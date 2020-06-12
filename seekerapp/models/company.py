from django.db import models
from .seeker import Seeker
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
class Company(SafeDeleteModel): 
    _safedelete_policy = SOFT_DELETE
    seeker = models.ForeignKey(Seeker, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    notes = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=55)
    isFollowedUp = models.BooleanField(max_length=55, null=True)