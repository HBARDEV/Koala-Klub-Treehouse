# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

User = get_user_model()



@login_required
@confirmed_otp_device_required
@permission_required({'users.view_customuser'}, raise_exception=True)
def user_details(request,id):
	user_obj=get_object_or_404(User,id=id)
	context={
		"user_obj":user_obj,
		"user_group_perms":user_obj.get_group_permissions(),
		"user_perms":user_obj.get_user_permissions(),
		"page_title":"User Details"
	}

	return render(request,"chrev/modules/user-details.html",context)