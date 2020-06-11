from django.db import models
from .company import Company
class Employee(models.Model): 
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    position = models.CharField(max_length=55)
    notes = models.CharField(max_length=255, null=True)
    isContacted = models.BooleanField(max_length=55, null=True)