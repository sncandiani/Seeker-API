from django.db import models 

class InterviewType(models.Model): 
    name = models.CharField(max_length=55)