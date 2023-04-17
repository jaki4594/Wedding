from django.db import models

# Create your models here.
class Guests(models.Model):
    
    name = models.CharField(max_length=200)
    number_of_guests = models.IntegerField(default=0)
    message = models.TextField()

    def __str__(self):
        return self.name

class Gifts(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

class Countdown(models.Model):
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)