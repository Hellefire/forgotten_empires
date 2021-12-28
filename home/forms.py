from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    terms = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'value': 1}),
        label=("I agree to Forgotten Empires Terms and Conditions of use"))
    use_required_attribute = False

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = settings.INVALID_LOGIN_ERROR
        self.fields['terms'].error_messages['required'] = \
            settings.NO_TERMS_ERROR
