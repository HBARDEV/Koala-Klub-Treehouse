






# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.fields.enums import Country

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from enumfields import EnumField


class AddressModel(models.Model):

    address = models.CharField(_('address'),max_length=250, blank=True)
    country = EnumField(Country, max_length=2, blank=True, null=True, verbose_name=_('country'))
    address_line_1 = models.CharField(_('address line one'),max_length=200, blank=True)
    address_line_2 = models.CharField(_('address line two'),max_length=200, blank=True)
    address_line_3 = models.CharField(_('address line three'),max_length=200, blank=True)
    city = models.CharField(_('city'),max_length=50, blank=True)
    locality = models.CharField(_('locality'),max_length=50, blank=True)
    postcode = models.CharField(_('postcode'),max_length=20, blank=True)

    class Meta:
        abstract = True