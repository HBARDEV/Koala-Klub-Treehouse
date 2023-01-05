# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from tasks.tasks import create_hedera_wallet

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_otp.plugins.otp_totp.models import TOTPDevice


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        '''
        Create a One time password object
        '''
        TOTPDevice.objects.create(
            user = instance,
            name = settings.COMPANY_NAME,
            confirmed=False
            )

        '''
        Create a new Hedera wallet
        '''
        create_hedera_wallet.delay(instance)