# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.contrib import messages


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
@permission_required({'auth.view_group','auth.add_group'}, raise_exception=True)
def group_add(request):
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Group Created Successfully')
			return redirect('users:groups')
		else:
			messages.warning(request,'Name Already Exist')
			return render(request, 'chrev/modules/group-add.html',{'form': form, 'page_title':'Add Group'})
	else:
		form = GroupForm()
		return render(request, 'chrev/modules/group-add.html',{'form': form, "page_title":"Add Group"})