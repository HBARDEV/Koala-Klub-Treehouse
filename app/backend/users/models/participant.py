# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from datetime import date

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
    TitleDescriptionModel,
    BaseUserModel
)
from utils.fields.enums import Gender, Ethnicity
from utils.validators import RegexValidator


# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from enumfields import EnumField

User = get_user_model()

#This is the new custom user model
class Participant(
    TimeStampedModel, 
    ActivatorModel,
    TitleDescriptionModel,
    BaseUserModel,
    Model
    ):

    '''
    Participant
    Used to store user participants (children)
    '''

    user = models.ForeignKey(
        User, 
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL,
        verbose_name=_('user'))

    school = models.CharField(_('school'),max_length=300,blank=True)

    ethnicity = EnumField(Ethnicity, blank=True, null=True, verbose_name=_('ethnicity'),max_length=100)
    disabilities = models.TextField(_('disabilities'),max_length=500,blank=True)
    medical = models.TextField(_('medical'),max_length=500,blank=True)
    behavioral = models.TextField(_('behavioral'),max_length=500,blank=True)
    educational = models.TextField(_('educational'),max_length=500,blank=True)

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

    pickup_pin = models.CharField(_('pickup pin'),validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Pickup pin must be entered in the format: '1234'. Up to 4 digits allowed."
            )
        ], 
        max_length=4, 
        blank=True,
        null=True)

