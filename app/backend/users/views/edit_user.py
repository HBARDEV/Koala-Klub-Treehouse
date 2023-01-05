# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import EditUserForm

User = get_user_model()

@login_required
@confirmed_otp_device_required
@permission_required({'users.view_customuser','users.change_customuser'}, raise_exception=True)
def edit_user(request,id):
	user_obj = get_object_or_404(User,id=id)
	if request.method == 'POST':
		form = EditUserForm(request.POST, request.FILES, instance=user_obj)
		if form.is_valid():
			user_obj = form.save()
			user_obj.groups.clear()
			for i in form.cleaned_data['groups']:
				user_obj.groups.add(i)
			return redirect('users:users')
	else:
		form = EditUserForm(instance=user_obj)
	return render(request, 'chrev/modules/add-user.html', {'form': form,"page_title":"Edit User"})
