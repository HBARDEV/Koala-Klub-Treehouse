# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os
from typing import Counter
import json
from datetime import datetime
from decimal import *


# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.apps import apps
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from core.models import Policy, FAQ
from tokens.models import CryptoToken
from users.models import CustomUser

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()
from djmoney.money import Money

User = get_user_model()
def get_model(model_name):
    app_name, model_name = model_name.split(".")
    Model = apps.get_model(app_name, model_name)
    return Model

def make_super_user(email, first_name, last_name, password):

    super_user= User.objects.create_superuser(
        email=email,
        first_name = first_name,
        last_name = last_name,
        password=password,
    )
    return super_user

def run():

    print ("***** Creating table rows *****")

    try:
        User.objects.get(email=os.environ.get("SUPER_USER_NAME"))
    except User.DoesNotExist:
        print ("***** Creating users *****")
        #create a new super user for the app  
        main = make_super_user(
            os.environ.get("SUPER_USER_EMAIL"),
            os.environ.get("SUPER_USER_FIRST_NAME"),
            os.environ.get("SUPER_USER_LAST_NAME"),
            os.environ.get("SUPER_USER_PASSWORD"))

        print ("***** finished creating users *****")

        json_files = [
            #load base models
            'db_config/policies.json',
        ]

        model_convertor = {
            "core.Policy": "core.Policy",
            "tokens.CryptoToken": "tokens.CryptoToken"
        }

        for json_file in json_files:
            print(f"***** Creating {json_file} *****")
            with open(json_file,"r",encoding='utf-8') as json_data:
                data = json.load(json_data)
                for c in data:
                    convert_model = model_convertor[c['model']]
                    match convert_model:

                        case "core.Policy":
                            obj, created= Policy.objects.get_or_create(
                                title = c["fields"]["title"],
                            )
                            obj.body= c["fields"]["body"]
                            obj.save()
                            if created:
                                print (f'***** Created {convert_model} {c["fields"]["title"]} *****')

                        case "tokens.CryptoToken":
                            obj, created= CryptoToken.objects.get_or_create(
                                title = c["fields"]["title"],
                            )
                            if created:
                                print (f'***** Created {convert_model} {c["fields"]["title"]} *****')
                        

        print ("***** Updating Site model *****")
        #adjust the Site model with the first host (localhost or domain)
        site = Site.objects.first()
        site.name = "Main"
        
        match settings.PRODUCTION:
            case 0:
                site.domain = "localhost:7070"
            case 1:
                os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")[0]
        site.save()

    print ("***** Done *****")

                   