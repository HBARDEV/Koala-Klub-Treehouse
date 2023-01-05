# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect


# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import OTPLoginForm

def otp_login_user(request):
	message=''
	if 'admin' in request.path:
		redirect_url = '/admin/'
	else:
		redirect_url = '/'
	if request.method == 'POST':
		form = OTPLoginForm(request.POST)
		if form.is_valid():
			user=form.login(request)
			if user is not None and user.is_active:
				login(request, user)
				usergroup = ','.join(request.user.groups.values_list('name',flat = True))
				messages.success(request,f'Welcome To {usergroup} Dashboard')
				next_url = request.GET.get('next')
				if next_url:
					return HttpResponseRedirect(next_url)
				else:
					return redirect(redirect_url)
			else:
				messages.warning(request,'User is Not Active')	
				
		else:
			messages.warning(request,'Form is Not valid! Please Check The Email, Password and OTP password')
			return render(request, 'chrev/modules/otp-login.html', context={'form': form})
	else:
		if request.user.is_authenticated:
			return redirect(redirect_url)
		form = OTPLoginForm()
	return render(request, 'chrev/modules/otp-login.html', context={'form': form})

