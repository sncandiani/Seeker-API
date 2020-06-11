from django.db import models 
from django.db.models import F
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Seeker(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)

    class Meta:
        ordering = (F('id').asc(nulls_last=True),)