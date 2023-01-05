# --------------------------------------------------------------
# Django  imports
# --------------------------------------------------------------
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as users_views
from users.forms import EmailValidationOnForgotPassword


from .admin import admin_site

handler400 = 'tree_house.views.handler400' 
handler403 = 'tree_house.views.handler403'
handler404 = 'tree_house.views.handler404'
handler500 = 'tree_house.views.handler500'
handler503 = 'tree_house.views.handler503'

urlpatterns = [
    path('admin/login/',users_views.login_user,name="admin-login"),
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace="core")),
    path('', include('users.urls', namespace="users")),

    path('comments/', include('tagging.urls')),
    path("__debug__/", include('debug_toolbar.urls')),
    

    path('reset_password/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword),name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

if not settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),

    ]
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Tree House Dashboard"  
admin.site.site_title  =  "Dashboard"
admin.site.index_title  =  "Dashboard"