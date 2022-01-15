from django import forms
from django.conf import settings

from alchemy.models import AlchemySpecialty
from character.models import (
    Character, Character_Skill, Character_Skill_Hand,
    Character_AlchemySlots, Character_SpellSlots
)
from generic.enums import handed
from magic.models import MagicSchool, MagicSubSchool
from skill.models import Skill, HandedSkill


def get_hand_choices():
    hand_choices = handed.all()
    empty_choice = ('', '-----')
    if empty_choice not in hand_choices:
        hand_choices.insert(0, empty_choice)
    return hand_choices


class CharacterBaseForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['name', 'chartype', 'player', 'race', 'subrace',
                  'charclass', 'deity', 'bank_iron', 'is_dead']

    def clean(self):
        cleaned_data = super(CharacterBaseForm, self).clean()
        chartype = cleaned_data.get('chartype')
        player = cleaned_data.get('player')
        if chartype == 'PC' and not player:
            self._errors['chartype'] = self.error_class(
                [settings.ERROR_PC_REQUIRES_PLAYER])
            self._errors['player'] = self.error_class(
                [settings.ERROR_PC_REQUIRES_PLAYER])
        return cleaned_data


class CharacterSkillForm(forms.Form):
    skill = forms.ModelChoiceField(queryset=Skill.objects.all())
    hand = forms.CharField(required=False)
    level = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        super(CharacterSkillForm, self).__init__(*args, **kwargs)
        self.fields['hand'] = forms.CharField(
            widget=forms.Select(choices=get_hand_choices()),
            required=False)
        if not self.is_bound:
            if 'skill' in kwargs and kwargs['skill'] is not None:
                self.fields['skill'].initial = kwargs['skill']
            if 'hand' in kwargs and kwargs['hand'] is not None:
                self.fields['hand'].initial = kwargs['hand']

    def clean(self):
        cleaned_data = super(CharacterSkillForm, self).clean()
        skill = cleaned_data.get('skill')
        hand = cleaned_data.get('hand')
        if skill.is_handed() and not hand:
            self._errors['hand'] = self.error_class(
                [settings.ERROR_HAND_REQUIRED])
        return cleaned_data

    def save(self, *args, **kwargs):
        character_id = kwargs.get('character_id')
        skill = self.cleaned_data.get('skill')
        hand = self.cleaned_data.get('hand')
        level = self.cleaned_data.get('level')
        char_skill = Character_Skill.objects.filter(
            character_id=character_id, skill=skill).first()
        if skill and level:
            if level > 0:
                if char_skill:
                    char_skill.level = level
                    char_skill.save()
                else:
                    char_skill = Character_Skill.objects.create(
                        character_id=character_id, skill=skill, level=level)
                if skill.is_handed():
                    cs_hand = Character_Skill_Hand.objects.filter(
                        character_skill=char_skill, hand=hand).first()
                    if cs_hand:
                        cs_hand.level = level
                        cs_hand.save()
                    else:
                        Character_Skill_Hand.objects.create(
                            character_skill=char_skill, hand=hand, level=level)
                return char_skill
            else:
                if char_skill:
                    if skill.is_handed():
                        Character_Skill_Hand.objects.filter(
                            character_skill=char_skill, hand=hand).delete()
                    else:
                        char_skill.delete()
                return None
        return None


class CharacterAlchemyForm(forms.Form):
    specialty = forms.ModelChoiceField(
        queryset=AlchemySpecialty.objects.all(), required=False)
    level = forms.IntegerField(min_value=1, max_value=6)
    slots = forms.IntegerField(min_value=0)

    def clean(self):
        cleaned_data = super(CharacterAlchemyForm, self).clean()
        specialty = cleaned_data.get('specialty')
        level = cleaned_data.get('level')
        if level > 3 and not specialty:
            self._errors['specialty'] = self.error_class(
                [settings.ERROR_SPECIALTY_REQUIRED])
        return cleaned_data

    def save(self, *args, **kwargs):
        character_id = kwargs.get('character_id')
        specialty = self.cleaned_data.get('specialty')
        level = self.cleaned_data.get('level')
        slots = self.cleaned_data.get('slots')
        char_alchemy = Character_AlchemySlots.objects.filter(
            character_id=character_id, specialty=specialty,
            level=level).first()
        if level and slots:
            if slots > 0:
                if char_alchemy:
                    char_alchemy.slots = slots
                    char_alchemy.save()
                else:
                    char_alchemy = Character_AlchemySlots.objects.create(
                        character_id=character_id, specialty=specialty,
                        level=level, slots=slots)
                return char_alchemy
            else:
                if char_alchemy:
                    char_alchemy.delete()
                return None
        return None


class CharacterSpellForm(forms.Form):
    school = forms.ModelChoiceField(queryset=MagicSchool.objects.all())
    specialty = forms.ModelChoiceField(
        queryset=MagicSubSchool.objects.all(), required=False)
    level = forms.IntegerField(min_value=1, max_value=9)
    slots = forms.IntegerField(min_value=0)

    def clean(self):
        cleaned_data = super(CharacterSpellForm, self).clean()
        school = cleaned_data.get('school')
        specialty = cleaned_data.get('specialty')
        if specialty and specialty.magicschool != school:
            self._errors['specialty'] = self.error_class(
                [settings.ERROR_MAGIC_SUBSCHOOL_MISMATCH])
        return cleaned_data

    def save(self, *args, **kwargs):
        character_id = kwargs.get('character_id')
        school = self.cleaned_data.get('school')
        specialty = self.cleaned_data.get('specialty')
        level = self.cleaned_data.get('level')
        slots = self.cleaned_data.get('slots')
        char_spell = Character_SpellSlots.objects.filter(
            character_id=character_id, school=school,
            specialty=specialty, level=level).first()
        if school and level and slots:
            if slots > 0:
                if char_spell:
                    char_spell.slots = slots
                    char_spell.save()
                else:
                    char_spell = Character_SpellSlots.objects.create(
                        character_id=character_id, school=school,
                        specialty=specialty, level=level, slots=slots)
                return char_spell
            else:
                if char_spell:
                    char_spell.delete()
                return None
        return None
