# --------------------------------------------------------------
# Django  imports
# --------------------------------------------------------------
from django.contrib.sites.models import Site

# --------------------------------------------------------------
# Project  imports
# --------------------------------------------------------------
from core import models as core_models
from core import admin as core_admin
from users import models as users_models
from users import admin as users_admin

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.admin import OTPAdminSite


class OTPAdmin(OTPAdminSite):
    '''
    Used to change the look & feel of the One Time Password (OTP) admin site
    '''
    login_template = "admin/login.html"


admin_site = OTPAdmin(name="OTPAdmin")

'------------------Register models OTP Admin site ------------------------'

admin_site.register(TOTPDevice)
admin_site.register(Site)

#Register main models to OTP admin
admin_site.register(core_models.Policy, core_admin.PolicyAdmin)
admin_site.register(core_models.Contact, core_admin.ContactAdmin)
admin_site.register(users_models.CustomUser, users_admin.CustomUserAdmin)





