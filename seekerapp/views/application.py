from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from seekerapp.models import Application, Seeker


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        url = serializers.HyperlinkedIdentityField(
            view_name='application',
            lookup_field='id'
        )
        fields = ('id', 'company', 'position', 'applicationDate', 'seeker_id')
        depth = 1


class Applications(ViewSet):
    def list(self, request):
        applications = Application.objects.filter(seeker__user=request.auth.user)
        serializer = ApplicationSerializer(
            applications, many=True, context={'request': request})
        return Response(serializer.data)

    # Post to Companies table
    def create(self, request):
        new_application = Application()
        seeker = Seeker.objects.get(user=request.auth.user)
        new_application.company = request.data["company"]
        new_application.position = request.data["position"]
        new_application.applicationDate = request.data["applicationDate"]
        new_application.seeker = seeker
        
        new_application.save()

        serializer = ApplicationSerializer(
            new_application, context={'request': request}
        )

        return Response(serializer.data)
   
    def retrieve(self, request, pk=None):
        try:
            application = Application.objects.get(pk=pk)
            serializer = ApplicationSerializer(
                application, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
     
    def update(self, request, pk=None): 
        application = Application.objects.get(pk=pk)
        seeker = Seeker.objects.get(user=request.auth.user)
        application.applicationDate = request.data["applicationDate"]
        application.company = request.data["company"]
        application.seeker = seeker
        application.position = request.data["position"]

        application.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)



    def delete(self, request, pk=None):
        try:
            application = Application.objects.get(pk=pk)
            application.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Application.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  

