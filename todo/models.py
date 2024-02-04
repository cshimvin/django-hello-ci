""" import models from django DB """
from django.db import models

# Create your models here.


class Item(models.Model):
    """ Class for the to do list item name and boolean for done """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.name
