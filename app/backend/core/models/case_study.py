# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel, TitleSlugDescriptionModel



def case_study_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/case_studies/<slug>/<filename>
    return f'case_studies/{instance.slug}/{filename}'

class CaseStudy(
    TimeStampedModel,
    ActivatorModel, 
    TitleSlugDescriptionModel,
    Model):

    class Meta:
        verbose_name_plural = "Case studies"

    image = models.ImageField(_('image'),upload_to=case_study_directory_path, default="default_case_study_image.jpg")
    media = models.URLField(_('media'), blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/case_study/{self.slug}/'