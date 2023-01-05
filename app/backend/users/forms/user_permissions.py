# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPermissionsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_permissions',)