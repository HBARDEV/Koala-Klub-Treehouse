# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Count

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

User = get_user_model()


@login_required
@confirmed_otp_device_required
@permission_required({'auth.view_group'}, raise_exception=True)
def groups_list(request):
	context={
		"groups":Group.objects.annotate(user_count=Count('customuser',distinct=True)).annotate(perms_count=Count('permissions',distinct=True)),
		"colors":{'primary':'primary','success':'success','dark':'dark'},
		"page_title":"Groups"
	}
	
	return render(request, 'chrev/modules/group-list.html', context)