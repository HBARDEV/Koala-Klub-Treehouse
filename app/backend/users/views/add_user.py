# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import CustomUserForm

User = get_user_model()


@login_required
@confirmed_otp_device_required
@permission_required({'users.view_customuser','users.add_customuser'}, raise_exception=True)
def add_user(request):
	if request.method == 'POST':
		form = CustomUserForm(request.POST, request.FILES)
		if form.is_valid():
			user_obj = form.save()
			user_obj.groups.clear()
			for i in form.cleaned_data.get('groups'):
				user_obj.groups.add(i)
			messages.success(request,f'{user_obj.first_name} {user_obj.last_name} is created successfully')
			return redirect('users:users')
	else:
		form = CustomUserForm()		
	return render(request, 'chrev/modules/add-user.html', {'form': form,"page_title":"Add User"})