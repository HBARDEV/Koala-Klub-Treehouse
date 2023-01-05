# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from ckeditor.fields import RichTextField


class RichTextModel(models.Model):
    """
    RichTextModel

    An abstract base class model that provides self-managed "description" field
    using ck_editor.
    """
    description = RichTextField(
        _('description'),
        blank=True,
        null=True
        )
        
    class Meta:
        abstract = True