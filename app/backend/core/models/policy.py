# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel, TitleSlugDescriptionModel


class Policy(
    TimeStampedModel,
    TitleSlugDescriptionModel,
    ActivatorModel,
    Model
    ):
    '''
    Our Policy model. This is used to create policy pages such as cookie and privacy
    '''

    class Meta:
        verbose_name = "Policy"
        verbose_name_plural = "Policies"
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f"/policy/{self.slug}"
