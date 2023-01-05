# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth.models import  Permission
from django.core.paginator import Paginator

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required



@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_permission'}, raise_exception=True)
def permissions(request):
	permission_list = Permission.objects.all()
	paginator = Paginator(permission_list, 5) # Show 5 permission per page.
	context={
		"permissions_obj" : paginator.get_page(request.GET.get('page')),
		"page_title":"Permissions"
	}
	
	return render(request, 'chrev/modules/permissions.html',context)