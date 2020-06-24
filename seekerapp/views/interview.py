from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework import serializers
from rest_framework import status
from seekerapp.models import Interview, InterviewType, Company, Employee

class InterviewSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Interview
        url = serializers.HyperlinkedIdentityField(
            view_name='interview', 
            lookup_field='id'
        )
        fields = ('id', 'interviewDate', 'notes', 'company_id', 'employee_id', 'interviewType_id') 
        depth = 1
class Interviews(ViewSet): 
    def list(self, request): 
        interviews = Interview.objects.filter(company__seeker__user=request.auth.user)
        serializer = InterviewSerializer(
            interviews, many = True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None): 
        try: 
            interview = Interview.objects.get(pk=pk)
            serializer = InterviewSerializer(
                interview, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)

    # Create an interview with or without an employee
    def create(self, request): 
        new_interview = Interview()
        company = Company.objects.get(pk=request.data["company_id"])
        interviewType = InterviewType.objects.get(pk=request.data["interviewType_id"])
        # Checks to determine if the employee id is specified 
        if "employee_id" in request.data:
            employee = Employee.objects.get(pk=request.data["employee_id"])
            new_interview.interviewDate = request.data["interviewDate"]
            new_interview.notes = request.data["notes"]
            new_interview.company = company 
            new_interview.employee = employee 
            new_interview.interviewType = interviewType 
        # If not, it'll keep the employee id value null 
        else: 
            new_interview.interviewDate = request.data["interviewDate"]
            new_interview.notes = request.data["notes"]
            new_interview.company = company 
            new_interview.interviewType = interviewType 


        new_interview.save()

        serializer = InterviewSerializer( 
            new_interview, context={'request': request}
        )
        return Response(serializer.data)
    
    # Hard delete an interview
    def delete(self, request, pk=None): 
        interview = Interview.objects.get(pk=pk)
        interview.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


    # Can update with or without employee 
    def update(self, request, pk=None): 
        interview = Interview.objects.get(pk=pk)
        company = Company.objects.get(pk=request.data["company_id"])
        interviewType = InterviewType.objects.get(pk=request.data["interviewType_id"])
    # REPETITIVE CODE !!! TO FIX 
        if "employee_id" in request.data:
            employee = Employee.objects.get(pk=request.data["employee_id"])
            interview.interviewDate = request.data["interviewDate"]
            interview.notes = request.data["notes"]
            interview.company = company 
            interview.employee = employee 
            interview.interviewType = interviewType 
        else: 
            interview.interviewDate = request.data["interviewDate"]
            interview.notes = request.data["notes"]
            interview.company = company 
            interview.interviewType = interviewType 
            interview.employee = None

        interview.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

        

