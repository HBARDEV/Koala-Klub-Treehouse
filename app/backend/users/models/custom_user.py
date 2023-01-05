# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from datetime import date

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
    BaseUserModel
)
from utils.validators import RegexValidator

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.managers import CustomUserManager

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_otp import devices_for_user
from enumfields import EnumField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<email>/<filename>
    return f'{instance.email}/{filename}'


#This is the new custom user model
class CustomUser(AbstractBaseUser, BaseUserModel ,Model, PermissionsMixin):

    '''
    CustomUser
    This is our custom user model.
    We are extending the built-in User model in Django.
    '''
    HEAD_COACH = 1
    COACH = 2
    SQUADDIE = 3
    ELITE_SQUADDIE = 4 
    FAN = 5 
      
    ROLE_CHOICES = (
        (HEAD_COACH, 'Head coach'),
        (COACH, 'Coach'),
        (SQUADDIE, 'Squaddie'),
        (ELITE_SQUADDIE, 'Elite squaddie'),
        (FAN, 'Fan'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    email = models.EmailField(_('email address'),unique=True)

    avatar = models.ImageField(_('avatar'),upload_to=user_directory_path, default="default_avatar.jpg")

    dob = models.DateTimeField(_('date of birth'),blank=True,null=True)

    def calculate_age(self):
        born = self.dob
        today = date.today()

        try:
            birthday = born.replace(year = today.year)
    
        # raised when birth date is February 29
        # and the current year is not a leap year
        except ValueError:
            birthday = born.replace(year = today.year,
                    month = born.month + 1, day = 1)
    
        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

  
    phone_number = models.CharField(_('phone number'),validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ], 
        max_length=17, 
        blank=True)
    
    groups = models.ManyToManyField(Group,blank=True)
    about = models.TextField(_('about'),max_length=500,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    two_factor_authentication_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name','last_name']

    account_id = models.CharField(max_length=100, blank=True, null=True)
    public_key = models.CharField(max_length=100, blank=True, null=True)
    private_key = models.CharField(max_length=100, blank=True, null=True)
    
    def has_confirmed_device(self, confirmed=True):
        try:
            otp = [d for d in devices_for_user(self, confirmed)][0]
            return True
        except IndexError:
            return False


    def get_otp_device(self):
        try:
            otp = [d for d in devices_for_user(self, confirmed=False)][0]
        except IndexError:
            otp = [d for d in devices_for_user(self)][0]
        return otp

    def manage_two_factor_auth(self, action=True):
        otp = self.get_otp_device()
        if action:
            self.two_factor_authentication_active = True
        else:
            self.two_factor_authentication_active = False
            otp.confirmed = False
        otp.save()
        self.save()