# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic


class OurStoryView(generic.TemplateView):
    """
    TemplateView used for our our story page.

    **Template:**

    :template:`core/our_story.html`
    """
    template_name = "core/our_story.html"