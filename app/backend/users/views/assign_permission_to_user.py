# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import  render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required 
from django.http import JsonResponse

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import UserPermissionsForm

User = get_user_model()

@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_permission','auth.add_permission','auth.change_permission'}, raise_exception=True)
def assign_permissions_to_user(request,id):
	user_obj = get_object_or_404(User,id=id)
	if request.method == 'POST':
		queryDict = request.POST
		data = dict(queryDict)

		if 'user_permissions[]' in data:
			user_obj.user_permissions.clear()
			user_obj.user_permissions.set(data['user_permissions[]'])
		else:
			user_obj.user_permissions.clear()
		response = JsonResponse({"success": "Save Successfully"})
		response.status_code = 200
		return response

	else:
		form = UserPermissionsForm(instance=user_obj)
	return render(request, 'chrev/modules/assign_permissions_to_user.html',{'form':form,"page_title":"Assign Permissions"})