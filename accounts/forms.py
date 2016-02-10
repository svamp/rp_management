#!/usr/bin/python
# -*- coding: utf-8 -*-
from userena.forms import SignupFormOnlyEmail
from userena import settings as userena_settings
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
import random

class CustomSignupForm(SignupFormOnlyEmail):
	"""custom SignupForm"""
	def save(self):
		new_user = super(CustomSignupForm, self).save()
		if new_user.username.isdigit():
			new_user = CustomSignupForm.regenerate_username(new_user)
			new_user.save()
		return new_user

	@classmethod
	def regenerate_username(cls, new_user):
		""" Generate a random username that also contains letters, not only digits. """
		is_username_taken = False
		while new_user.username.isdigit() or is_username_taken:
			username = sha_constructor(str(random.random())).hexdigest()[:5]
			new_user.username = username
			is_username_taken = User.objects.filter(username__iexact=username).exists()
		return new_user

class AuthenticationForm(forms.Form):
    identification = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'required form-control',
                                      'placeholder': _(u"Enter your e-mail address")}),
        label=_(u"E-mail address"),
        max_length=75,
        error_messages={'required': _(u"Please supply your email.")}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'required form-control',
                                          'placeholder': _(u"Enter your password")},
                                   render_value=False),
        label=_("Password"),
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label=_(u'Remember me for %(days)s') % {'days': _(userena_settings.USERENA_REMEMBER_ME_DAYS[0])},
        required=False
    )

    def clean(self):
        """
        Checks for the identification and password.

        If the combination can't be found will raise an invalid sign in error.
        """
        identification = self.cleaned_data.get('identification')
        password = self.cleaned_data.get('password')

        if identification and password:
            user = authenticate(identification=identification, password=password)
            if user is None:
                error_msg = _(u"Please enter a correct username or email and password. Note that both fields are case-sensitive.")
                raise forms.ValidationError(error_msg)
        return self.cleaned_data

		