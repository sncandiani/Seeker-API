from django.db import models 
from .company import Company
from .employee import Employee
from .interviewtype import InterviewType
class Interview(models.Model): 
    interviewDate = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True)
    interviewType = models.ForeignKey(InterviewType, on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=255, null=True)
