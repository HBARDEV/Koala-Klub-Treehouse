# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from django_otp import match_token


User = get_user_model()



class OTPLoginForm(forms.Form):
    email =  forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    otp_token = forms.CharField(required=False, widget=forms.TextInput(attrs={'autocomplete': 'off'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        token = self.cleaned_data.get("otp_token")
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        else:
            device = match_token(user, token)
            if device is None:
                raise forms.ValidationError('Invalid token. Please make sure you have entered it correctly.')
            
        return self.cleaned_data
        
    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user