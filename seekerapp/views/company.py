from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from seekerapp.models import Seeker, Company

class CompanySerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Company
        url = serializers.HyperlinkedIdentityField(
            view_name='company',
            lookup_field='id'
        )
        fields = ('id', 'name', 'city', 'state', 'industry', 'seeker_id', 'notes', 'isFollowedUp')
        depth = 1

class Companies(ViewSet): 

    # List all companies in the Company table
    def list(self, request): 
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True, context={'request': request})
        return Response(serializer.data)

    # Post to Companies table
    def create(self, request): 
        new_company = Company()
        # Associated seeker data is requested
        seeker = Seeker.objects.get(user=request.auth.user)
        # The rest of the data for the incoming company object will be taken in from the form
        new_company.name = request.data["name"]
        new_company.city = request.data["city"]
        new_company.state = request.data["state"]
        new_company.industry = request.data["industry"]
        new_company.seeker = seeker
        # Notes do not appear as options on create, only on update
        new_company.save()

        serializer = CompanySerializer(
            new_company, context={'request': request}
        )

        return Response(serializer.data)
    # Retrieve specific company
    def retrieve(self, request, pk=None): 
        try: 
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(
                company, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)

    # Soft delete specific company using Django Safedelete
    def delete(self, request, pk=None):
        try:
            # Retrieve the specific company that will be deleted
            company = Company.objects.get(pk=pk)
            # Company deleted field will return when the company was deleted
            # Will not be removed from the database
            company.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except company.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Update a specific company on put request, does not update isFollowedUp!
    def update(self, request, pk=None): 
        company = Company.objects.get(pk=pk)
        seeker = Seeker.objects.get(user=request.auth.user)    
        company.name = request.data["name"]
        company.city = request.data["city"]
        company.state = request.data["state"]
        company.industry = request.data["industry"]
        # Notes can be updated from null to user created value
        company.notes = request.data["notes"]
        company.seeker = seeker
        company.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    # Patch to change follow up ONLY
    def patch(self, request, pk=None):
            try:  

                    company = Company.objects.get(pk=pk)
                    company.isFollowedUp = request.data["isFollowedUp"]
                    serializer = CompanySerializer(company, context={'request': request}, partial=True)
                    company.save()
                    return Response(status=status.HTTP_201_CREATED, data=serializer.data)

            except Company.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

