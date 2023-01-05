# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel
from utils.validators import RegexValidator



class Contact(
    TimeStampedModel,
    ActivatorModel, 
    Model):

	class Meta:
		verbose_name_plural = "Contacts"

	name = models.CharField(_('name'),max_length=100)

	phone_number = models.CharField(_('phone number'),validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ], 
        max_length=17, 
        blank=True)

	email = models.EmailField(_('email'))
	message = models.TextField(_('message'),max_length=1000)

	def __str__(self):
		return f'{self.name}'