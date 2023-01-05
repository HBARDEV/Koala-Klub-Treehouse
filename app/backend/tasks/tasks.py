# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.apps import apps

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from celery import shared_task
from celery.utils.log import get_task_logger

User = get_user_model()
 
logger = get_task_logger(__name__)


@shared_task(bind=True)
def create_email(self, user_id: int, internal=True, **kwargs):
    '''
    Used to create an email and send via a selection of templates
    '''
    context = kwargs.get("context", {})
    email_account = kwargs.get("email_account")
    subject = kwargs.get("subject", "")
    email = kwargs.get("email")
    template = kwargs.get("template")
    cc_email = kwargs.get("cc_email", [])
    bcc_email = kwargs.get("bcc_email", [])
    match internal:
        case False:
            try:
                user = User.objects.get(id=user_id)
                context["email"] = user.email
            except User.DoesNotExist:
                return f"Task: Send email to [{email}]: Fail - User does not exist"
    
    site_id = settings.SITE_ID
    current_site = Site.objects.get(id = site_id).domain
    if settings.PRODUCTION:
        protocol = "https://"
    else:
        protocol = "http://"
    context["domain"] = f'{protocol}{current_site}'
    context["support_email"] = settings.SUPPORT_EMAIL
    context["logo"] = 'https://tree_house-spaces.ams3.digitaloceanspaces.com/static/branding/email_logo.png' 
    context["process_time"] = settings.PROCESS_TIME_DELAY
    
    email_accounts = {
        "donotreply": {
            'name': settings.EMAIL_HOST_USER,
            'password':settings.EMAIL_HOST_PASSWORD,
            'from':settings.EMAIL_HOST_USER,
            'display_name': settings.EMAIL_DISPLAY_NAME},
    }
 
    html_content = render_to_string(template, context ) # render with dynamic value
    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
 
    with get_connection(
            host= settings.EMAIL_HOST,
            port= settings.EMAIL_PORT,
            username=email_accounts[email_account]["name"],
            password=email_accounts[email_account]["password"],
            use_tls=settings.EMAIL_USE_TLS,
        ) as connection:
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                f'{email_accounts[email_account]["display_name"]} <{email_accounts[email_account]["from"]}>',
                [email],
                cc=cc_email,
                bcc=bcc_email,
                connection=connection)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    return f"Task: Send email to [{email}]: Success"
 

@shared_task(bind=True)
def lock_for_processing(self, object_id, app_name, model):
    '''
    Used to lock an object after a processing delay
    '''
    Model = apps.get_model(app_name, model)
    obj = Model.objects.get(id = object_id)
    obj.locked_for_processing = True
    obj.save()
    return f"Task: Lock for processing. Model: {obj._meta.app_label}:{obj._meta.object_name} ID: {obj.id} -  Success"


 

