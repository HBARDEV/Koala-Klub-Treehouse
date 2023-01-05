# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from django_otp import devices_for_user

User = get_user_model()

@login_required
def register_device(request):
	try:
		user = request.user
		otp = [[d.pk,d.config_url,d ] for d in devices_for_user(user, confirmed=False)][0]
	except IndexError:
		return redirect('/')

	if request.method == 'POST':
		user.manager_two_factor_auth()
		response = JsonResponse({"success": "All good"})
		response.status_code = 200
		return response
	return render(request, 'chrev/modules/register-device.html', context={'otp': otp})
