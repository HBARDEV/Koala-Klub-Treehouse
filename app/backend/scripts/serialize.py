

from core.models import Policy, FAQ
from users.models import UserProfile, UserToken
from django.contrib.auth import get_user_model
from django.core import serializers
import json
User = get_user_model()
def run():
    all_objects = [
        *User.objects.all(),
        *Policy.objects.all(),
        *FAQ.objects.all(),
        *UserProfile.objects.all(),
        *UserToken.objects.all(),
        ]
    data = serializers.serialize("json", all_objects)
    data = json.loads(data)
    with open("full_db.json", "w") as write_file:
        json.dump(data, write_file, indent=4, sort_keys=True)
    return "ALREADY LOADED"


