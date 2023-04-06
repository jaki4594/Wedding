from django.db import models

# Create your models here.
class Guests(models.Model):
    name = models.CharField(max_length=200)
    number_of_guests = models.IntegerField(default=0)
    message = models.TextField()

class Gifts(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)