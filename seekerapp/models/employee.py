from django.db import models
from .company import Company
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
class Employee(SafeDeleteModel): 
    _safedelete_policy = SOFT_DELETE
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    position = models.CharField(max_length=55)
    notes = models.CharField(max_length=255, null=True)
    isContacted = models.BooleanField(max_length=55, null=True)