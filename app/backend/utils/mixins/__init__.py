from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


def reCAPTCHAValidation(token):

	''' reCAPTCHA validation '''
	result = requests.post(
		'https://www.google.com/recaptcha/api/siteverify',
		 data={
		 	'secret': settings.RECAPTCHA_PRIVATE_KEY,
			'response': token
		 })

	return result.json()



'''
Handles form error that are passed back to AJAX calls
'''
def FormErrors(*args):
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message




'''
Mixin to ajaxify django form - can be over written in view by calling form_valid method
'''
class AjaxFormMixin(object):
	
	def form_invalid(self, form):
		response = super(AjaxFormMixin, self).form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		return response

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if self.request.is_ajax():
			form.save()
			return JsonResponse({'message':'Success'})
		return response


'''
Used to append url parameters when redirecting users
'''
def RedirectParams(**kwargs):
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response

