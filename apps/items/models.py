"""Imports"""

from django.db import models
from django.conf import settings

from config.managers import ItemManager

# Create your models here.

class Item(models.Model):
    """
    Model to collect all items for the application and
    send to the database
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    reserve_price = models.IntegerField()
    photo = models.CharField(max_length=10, default="Photo here") # TODO

    objects = ItemManager()
