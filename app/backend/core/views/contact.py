# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.contrib import messages
from django.conf import settings

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import AjaxFormMixin, reCAPTCHAValidation

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.forms import ContactForm


class ContactView(AjaxFormMixin, generic.FormView):

    """
    FormView used for our home page.

    **Template:**

    :template:`core/contact.html`
    """
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_site_key"] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    #over write the mixin logic to get, check and save reCAPTURE score
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            token = form.cleaned_data.get('token')
            captcha = reCAPTCHAValidation(token)
            if captcha["success"]:
                obj = form.save()
                obj.captcha_score = float(captcha["score"])
                obj.save()
                data = {'result': 'Success', 'message': "Thank your for contact us"}
                return JsonResponse(data)
            else:
                data = {'result': "Error", 'message': "There was an error, please try again"}
                return JsonResponse(data)
        return response