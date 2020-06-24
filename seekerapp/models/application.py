from django.db import models 

class Application(models.Model): 
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
