# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required


@login_required
@confirmed_otp_device_required
def deactivate_two_factor_auth(request):
	user = request.user 
	user.manager_two_factor_auth(action= False)
	messages.success(request,"2FA deactivated")
	return redirect('users:app-profile')