# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import confirmed_otp_device_required

User = get_user_model()


@login_required
@confirmed_otp_device_required
@permission_required({'users.view_customuser'}, raise_exception=True)
def users(request):
	user_list = User.objects.filter(is_superuser=False).order_by('groups__name')
	paginator = Paginator(user_list, 7)
	context={
		"user_list" : paginator.get_page(request.GET.get('page')),
		"page_title":"Users"
	}
	return render(request, "chrev/modules/users.html",context)
