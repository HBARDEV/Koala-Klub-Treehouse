# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

@login_required
@confirmed_otp_device_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)

		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request, user)
			messages.success(request,'Password Update Successfully')
			return redirect('/password/')
		else:
			messages.warning(request,'Form is not valid')
		
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'chrev/modules/change-password.html', {'form': form, "page_title":"Change Password"})

