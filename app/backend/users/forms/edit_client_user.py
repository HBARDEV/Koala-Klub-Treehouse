# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.fields.enums import Gender
from utils.validators import RegexValidator

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from enumfields import EnumField

User = get_user_model()


class EditClientUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    dob = forms.DateTimeField(required=False)
    phone_number = forms.CharField(required=True, 
        validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ])

    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),required=False)
   
    gender = EnumField(Gender).formfield()

    class Meta:
        model = User
        fields = ('email',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'gender',
                  'avatar',
                  'dob',
                  'phone_number',
                  'groups',
                  'about',
                )

        widgets = {
            'avatar': forms.FileInput(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save()
        return user

