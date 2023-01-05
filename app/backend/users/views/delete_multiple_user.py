# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

User = get_user_model()

@login_required
@confirmed_otp_device_required
@permission_required({'users.view_customuser','users.delete_customuser'},raise_exception=True)
def delete_multiple_user(request):
	id_list=request.POST.getlist('id[]')
	id_list = [i for i in id_list if i != '']
	for id in id_list:
		user_obj = User.objects.get(pk=id)
		user_obj.delete()

	response = JsonResponse({"success": 'user deleted successfully'})
	response.status_code = 200
	return response