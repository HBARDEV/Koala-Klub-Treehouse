# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel, TitleSlugDescriptionModel



def news_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/news/<slug>/<filename>
    return f'/news/{instance.slug}/{filename}'

class News(
    TimeStampedModel,
    ActivatorModel, 
    TitleSlugDescriptionModel,
    Model):

    class Meta:
        verbose_name_plural = "Case studies"

    image = models.ImageField(_('image'),upload_to=news_directory_path, default="default_news_image.jpg")
    url = models.URLField(_('news url'))

    def __str__(self):
        return f'{self.title}'
