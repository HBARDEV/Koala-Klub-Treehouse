# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os
from datetime import timedelta

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from celery import Celery

 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree_house.conf.prod')
app = Celery('tree_house')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Europe/London'

app.conf.beat_schedule = {
    "sync_treasury_wallet": {
        "task": "tasks.tasks.sync_treasury_wallet",
        "schedule": timedelta(days=1),
    },
}
 
app.autodiscover_tasks()
