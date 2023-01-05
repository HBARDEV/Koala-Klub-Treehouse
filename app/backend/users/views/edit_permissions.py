# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import  render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth.models import  Permission
from django.core.paginator import Paginator

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import PermissionsForm

@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_permission','auth.change_permission'}, raise_exception=True)
def edit_permissions(request,id):
	perm_obj = get_object_or_404(Permission,id=id)
	if request.method == 'POST':
		form = PermissionsForm(request.POST,instance=perm_obj)
		if form.is_valid():
			form.save()
			return redirect('users:permissions')
	else:
		form = PermissionsForm(instance=perm_obj)
		return render(request, 'chrev/modules/edit-permissions.html',{'form': form, "page_title":"Edit Permissions"})