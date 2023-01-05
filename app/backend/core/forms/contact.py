# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import ReCaptchaMixin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Contact



class ContactForm(forms.ModelForm, ReCaptchaMixin):
    '''
    Basic model-form for our contact model
    '''

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Full name..',
            'class': 'form-control'
            }))
    phone_number = forms.CharField(max_length=15, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Telephone number..',
            'class': 'form-control'
            }))
    email = forms.EmailField(max_length=254, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            'class': 'form-control'
            }))
    message = forms.CharField(max_length=1000, required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': '*Message..',
            'class': 'form-control'
            }))


    class Meta:
        model = Contact
        fields = ('name', 'phone_number', 'email', 'message',)