# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import JsonResponse

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import GroupForm


User = get_user_model()


@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_group','auth.change_group'}, raise_exception=True)
def group_edit(request,id):
	group_obj = get_object_or_404(Group,id=id)

	if request.method == 'POST':
		queryDict = request.POST
		data = dict(queryDict)

		try:
			group_obj.name = data['name'][0]
			group_obj.save()
		except:
			response = JsonResponse({"error": "Group Name already exist"})
			response.status_code = 403
			return response

		if 'permissions[]' in data:
			group_obj.permissions.clear()
			group_obj.permissions.set(data['permissions[]'])
		else:
			group_obj.permissions.clear()

	
		response = JsonResponse({"success": "Save Successfully"})
		response.status_code = 200
		return response

	else:
		form = GroupForm(instance=group_obj)
	
	return render(request, 'chrev/modules/group-edit.html',{'form': form, "page_title":"Edit Group"})