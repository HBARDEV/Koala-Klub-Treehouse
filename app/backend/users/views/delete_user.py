# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

User = get_user_model()


@login_required
@confirmed_otp_device_required
@permission_required({'users.view_customuser','users.delete_customuser'},raise_exception=True)
def delete_user(request,id):
	u = User.objects.get(id=id)
	u.delete()
	messages.success(request, "User deleted successfully") 
	return redirect('users:users')
