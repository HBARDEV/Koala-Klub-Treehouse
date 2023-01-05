# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel, TitleSlugDescriptionModel


def experience_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/experiences/<slug>/<filename>
    return f'experiences/{instance.slug}/{filename}'


class Experience(
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
    Model):

    class Meta:
        verbose_name_plural = "Experiences"

    image = models.ImageField(_('image'),upload_to=experience_directory_path, default="default_experience_image.jpg")
    media = models.URLField(_('media'), blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/experience/{self.slug}/'
    