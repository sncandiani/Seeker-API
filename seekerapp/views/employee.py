from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from seekerapp.models import Company, Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Employee
        url = serializers.HyperlinkedIdentityField(
            view_name='employee',
            lookup_field='id'
        )
        fields = ('id', 'firstName', 'lastName', 'position', 'notes', 'isContacted', 'company_id')
        depth = 1

class Employees(ViewSet):
    def list(self, request): 
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(
            employees, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None): 
        try: 
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(
                employee, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)


    def create(self, request): 
        new_employee = Employee()
        company = Company.objects.get(pk=request.data["company_id"])
        new_employee.company = company
        new_employee.firstName = request.data["firstName"]
        new_employee.lastName = request.data["lastName"]
        new_employee.position = request.data["position"]

        new_employee.save()

        serializer = EmployeeSerializer(
            new_employee, context={'request': request}
        )

        return Response(serializer.data)
