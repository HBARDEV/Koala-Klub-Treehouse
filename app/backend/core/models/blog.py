# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import TimeStampedModel, Model, ActivatorModel, TitleSlugDescriptionModel


def blog_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/news/<slug>/<filename>
    return f'/blog/{instance.slug}/{filename}'

class Blog(
    TimeStampedModel,
    ActivatorModel, 
    TitleSlugDescriptionModel,
    Model):

    class Meta:
        verbose_name_plural = "Blog"

    image = models.ImageField(_('image'),upload_to=blog_directory_path, default="default_blog_image.jpg")
    media = models.URLField(_('media'), blank=True, null=True)


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'
