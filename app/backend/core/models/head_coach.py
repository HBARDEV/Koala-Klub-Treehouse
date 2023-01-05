# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel, AddressModel, BaseUserModel
from utils.validators import RegexValidator
from utils.fields.enums import   OpportunityType, HighestQualification

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from enumfields import EnumField



class HeadCoach(
    TimeStampedModel,
    ActivatorModel, 
    AddressModel,
    BaseUserModel,
    Model):

    class Meta:
        verbose_name_plural = "Head Coach applications"

    email = models.EmailField(_('email'))
    
    opportunity_type = EnumField(OpportunityType, blank=True, null=True, verbose_name=_('opportunity type'), max_length=100)
    highest_qualification = EnumField(HighestQualification, blank=True, null=True, verbose_name=_('highest qualification'), max_length=100)
    relevant_experience = models.TextField(_('relevant experience'), max_length=1000, blank=True, null=True)
    how_did_you_hear = models.CharField(_('how did you hear'), max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'