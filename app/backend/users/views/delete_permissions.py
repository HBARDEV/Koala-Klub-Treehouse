# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import  render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth.models import  Permission
from django.contrib import messages

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required


@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_permission','auth.delete_permission'}, raise_exception=True)
def delete_permissions(request,id):
	perm_obj = get_object_or_404(Permission,id=id)
	perm_obj.delete()
	messages.success(request,'Permission Delete Successfully')
	return redirect('users:permissions')