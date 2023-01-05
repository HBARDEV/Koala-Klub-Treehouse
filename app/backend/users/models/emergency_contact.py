# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
    TimeStampedModel,
    ActivatorModel,
    BaseUserModel
)

from utils.validators import RegexValidator

User = get_user_model()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<email>/<filename>
    return f'{instance.email}/{filename}'


#This is the new custom user model
class EmergencyContact(TimeStampedModel, ActivatorModel,BaseUserModel, Model):

    '''
    EmergencyContact
    Used to store user emergency contact
    '''

    user = models.ForeignKey(
        User, 
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL,
        verbose_name=_('user'))

    phone_number = models.CharField(_('phone number'),validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ], 
        max_length=17, 
        blank=True)

