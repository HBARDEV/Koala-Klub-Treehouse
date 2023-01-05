# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from . import models 

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email')


@admin.register(models.Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    readonly_fields = ('slug',)
