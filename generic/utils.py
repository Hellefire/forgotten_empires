from django.contrib.auth.mixins import UserPassesTestMixin

from generic.enums import handed


class UserStaffMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_staff


def get_base_template_name(user):
    if user.is_staff:
        return 'gm_home.html'
    else:
        return 'player_home.html'


def get_hand_choices():
    choices = handed.all()
    empty_choice = ('', '-----')
    return choices.insert(0, empty_choice)
