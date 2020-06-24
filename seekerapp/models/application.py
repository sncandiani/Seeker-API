from django.db import models 
from .seeker import Seeker

class Application(models.Model): 
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    seeker = models.ForeignKey(Seeker, on_delete=models.DO_NOTHING, null=True)
