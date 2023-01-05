# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms


class ReCaptchaMixin:

    #reCAPTCHA token
    token = forms.CharField(
        widget=forms.HiddenInput())