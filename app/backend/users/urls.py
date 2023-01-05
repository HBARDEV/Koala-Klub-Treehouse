# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.urls import path

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from . import views

app_name = "users"

urlpatterns = [
    path('password/', views.change_password, name='change_password'),
    path('users/',views.users,name="users"),
	path('user-details/<uuid:id>/',views.user_details,name="user-details"),
	path('add-user/',views.add_user,name="add-user"),
	path('edit-user/<uuid:id>/',views.edit_user,name="edit-user"),
	path('delete-user/<uuid:id>/',views.delete_user,name="delete-user"),
	path('delete-multiple-user/',views.delete_multiple_user,name="delete-multiple-user"),
	path('register-device/',views.register_device,name="register-device"),
	path('deactivate-2fa/',views.deactivate_two_factor_auth,name="deactivate-2fa"),
	path('login/',views.login_user,name="login"),
	path('otp-login/',views.otp_login_user,name="otp-login"),
	path('logout/',views.logout,name="logout"),
	path('groups/',views.groups_list,name="groups"),
	path('group-edit/<int:id>/',views.group_edit,name="group-edit"),
	path('group-delete/<int:id>/',views.group_delete,name="group-delete"),
	path('group-add/',views.group_add,name="group-add"),
	path('permissions/',views.permissions,name="permissions"),
	path('edit-permissions/<int:id>/',views.edit_permissions,name="edit-permissions"),
	path('delete-permissions/<int:id>/',views.delete_permissions,name="delete-permissions"),
	path('assign-permissions-to-user/<int:id>/',views.assign_permissions_to_user,name="assign-permissions-to-user"),
	path('signup/',views.signup,name="signup"),
	path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]