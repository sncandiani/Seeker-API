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
    # List all employees
    def list(self, request): 
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(
            employees, many=True, context={'request': request}
        )
        return Response(serializer.data)
    # Retrieve specific employee
    def retrieve(self, request, pk=None): 
        try: 
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(
                employee, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)

    # Post employee without notes 
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
    # Soft delete on employee using django safedelete
    def delete(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
            
        except employee.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # Update employee wiht notes  
    def update(self, request, pk=None): 
        employee = Employee.objects.get(pk=pk)

        employee.firstName = request.data["firstName"]
        employee.lastName = request.data["lastName"]
        employee.position = request.data["position"]
        employee.notes = request.data["notes"]
        employee.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    # Patch isContacted , toggled on client side
    def patch(self, request, pk=None): 
        employee = Employee.objects.get(pk=pk)
        employee.isContacted = request.data["isContacted"]
        employee.save()
        serializer = EmployeeSerializer(
            employee, context={'request': request}, partial=True
        )
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

