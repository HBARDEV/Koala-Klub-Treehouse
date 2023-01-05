# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages


# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required


User = get_user_model()


@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_group','auth.delete_group'}, raise_exception=True)
def group_delete(request,id):
	g=get_object_or_404(Group,id=id)
	g.delete()
	messages.success(request,'Group Deleted Sucessfully')
	return redirect('users:groups')