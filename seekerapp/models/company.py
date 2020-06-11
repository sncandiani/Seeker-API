from django.db import models
from .seeker import Seeker
class Company(models.Model): 
    seeker = models.ForeignKey(Seeker, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    notes = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=55)
    isFollowedUp = models.BooleanField(max_length=55, null=True)