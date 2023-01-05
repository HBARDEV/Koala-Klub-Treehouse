# --------------------------------------------------------------
# Python imports
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
    TitleDescriptionModel
)

User = get_user_model()

#This is the new custom user model
class Qualification(TimeStampedModel, ActivatorModel,TitleDescriptionModel,Model):

    '''
    Qualification
    Used to store user qualification
    '''

    user = models.ForeignKey(
        User, 
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL,
        verbose_name=_('user'))

    expiry_date = models.DateTimeField(blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)

