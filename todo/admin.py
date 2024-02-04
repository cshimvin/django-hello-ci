""" Import required modules for django app """
from django.contrib import admin
from .models import Item

# Register your models here.

admin.site.register(Item)
