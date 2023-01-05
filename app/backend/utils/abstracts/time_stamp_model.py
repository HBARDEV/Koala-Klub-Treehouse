# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.fields import  CreationDateTimeField, ModificationDateTimeField


class TimeStampedModel(models.Model):
    """
    TimeStampedModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """

    creation_date = CreationDateTimeField(_('creation date'))
    update_date = ModificationDateTimeField(_('update_date'))

    def save(self, **kwargs):
        self.update_modified = kwargs.pop('update_date', getattr(self, 'update_date', True))
        super().save(**kwargs)

    class Meta:
        get_latest_by = 'update_date'
        abstract = True