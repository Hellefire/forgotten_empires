from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from character.forms import (
    CharacterBaseForm, 
    CharacterSkillForm, CharacterAlchemyForm, CharacterSpellForm
)
from character.models import Character, Character_Skill, Character_Skill_Hand
from generic.utils import UserStaffMixin, get_base_template_name
from skill.models import HandedSkill, Skill


class CharacterDetailView(LoginRequiredMixin, DetailView):
    model = Character
    template_name = "character_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['gm_view'] = user.is_staff
        context['extend'] = get_base_template_name(user)
        return context


class CharacterListView(LoginRequiredMixin, ListView):
    model = Character
    template_name = "character_list.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            characters = Character.objects.filter(player__is_active=True)
        else:
            if hasattr(user, 'player'):
                characters = Character.objects.filter(player=user.player)
            else:
                characters = Character.objects.none()
        return characters.order_by('player__name', 'name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['gm_view'] = user.is_staff
        context['extend'] = get_base_template_name(user)
        return context


def character_add(request):
    return render(request, 'terms.html')


def character_edit(request):
    return render(request, 'terms.html')


def set_base_data(character_id):
    base_data = {'skill': [], 'alchemy': [], 'spell': []}
    if character_id:
        character = Character.objects.get(id=character_id)
        char_skills = character.skills_dict()
        for skill_type, char_skill_list in char_skills['base'].items():
            for skill_dict in char_skill_list:
                char_skill_id = skill_dict['id']
                skill_id = skill_dict['skill_id']
                skill = Skill.objects.get(id=skill_id)
                level = skill_dict['level']
                if char_skill_id in char_skills['handed'].keys():
                    for hand, level in \
                            char_skills['handed'][char_skill_id].items():
                        skill_data = {
                            'skill': skill, 'hand': hand, 'level': level}
                        base_data['skill'].append(skill_data)
                else:
                    skill_data = {
                        'skill': skill, 'hand': None, 'level': level}
                    base_data['skill'].append(skill_data)
        char_slots = character.slots_dict()
        if 'alchemy' in char_slots:
            for alchemy in char_slots['alchemy']:
                base_data['alchemy'].append(alchemy)
        if 'spells' in char_slots:
            for spell in char_slots['spells']:
                base_data['spell'].append(spell)
    return base_data


def character_update_gm(request, character_id):
    character = None
    if character_id:
        character = Character.objects.get(id=character_id)
    base_data = set_base_data(character_id)
    SkillFormSet = formset_factory(CharacterSkillForm, extra=5)
    AlchemyFormSet = formset_factory(CharacterAlchemyForm, extra=5)
    SpellFormSet = formset_factory(CharacterSpellForm, extra=5)
    if request.method == 'POST':
        base_form = CharacterBaseForm(request.POST, instance=character)
        skill_formset = SkillFormSet(
            request.POST, initial=base_data['skill'], prefix='skill')
        alchemy_formset = AlchemyFormSet(
            request.POST, initial=base_data['alchemy'], prefix='alchemy')
        spell_formset = SpellFormSet(
            request.POST, initial=base_data['spell'], prefix='spell')
        if (
            base_form.is_valid() and skill_formset.is_valid() and
                alchemy_formset.is_valid() and spell_formset.is_valid()):
            char = base_form.save()
            for form in skill_formset:
                form.save(character_id=char.id)
            handed_skills = HandedSkill.objects.all()
            for handed_skill in handed_skills:
                char_skill = Character_Skill.objects.filter(
                    skill=handed_skill.skill, character_id=char.id).first()
                if char_skill:
                    total_skill = 0
                    char_hand_skills = Character_Skill_Hand.objects.filter(
                        character_skill=char_skill)
                    for hand_skill in char_hand_skills:
                        total_skill += hand_skill.level
                    if total_skill:
                        char_skill.level = total_skill
                        char_skill.save()
                    else:
                        char_skill.delete()
            for form in alchemy_formset:
                form.save(character_id=char.id)
            for form in spell_formset:
                form.save(character_id=char.id)

            if character:
                messages.success(request, settings.SUCCESS_CHARACTER_UPDATE)
            else:
                messages.success(request, settings.SUCCESS_CHARACTER_ADD)
            return HttpResponseRedirect(reverse('character_view', args=(char.id,)))
    else:
        base_form = CharacterBaseForm(instance=character)
        skill_formset = SkillFormSet(
            initial=base_data['skill'], prefix='skill')
        alchemy_formset = AlchemyFormSet(
            initial=base_data['alchemy'], prefix='alchemy')
        spell_formset = SpellFormSet(
            initial=base_data['spell'], prefix='spell')
    return render(request, 'character_update_gm.html', {
        'character': character, 'base_form': base_form, 'skill_formset': skill_formset,
        'alchemy_formset': alchemy_formset, 'spell_formset': spell_formset,
        'extend': get_base_template_name(request.user)
    })
