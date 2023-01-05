# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth import get_user_model

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

#Add User Form
class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    dob = forms.CharField(required=True)
    phone_number = forms.CharField(required=True, 
        validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ])
    
    GENDER_CHOICES = (
        ('','Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
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
                  'is_active',
                  'password1',
                  'password2',
                )
        widgets = {
            'avatar': forms.FileInput(),
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

