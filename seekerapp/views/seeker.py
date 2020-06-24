from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework import serializers
from rest_framework import status
from seekerapp.models import Seeker

class SeekerSerializer(serializers.HyperlinkedModelSerializer): 
     class Meta:
        model = Seeker
        url = serializers.HyperlinkedIdentityField(
            view_name='seeker', 
            lookup_field='id'
        )
        fields = ('id', 'user_id', 'user', 'city', 'state') 
        depth = 1

class Seekers(ViewSet):
    def list(self, request): 
        seekers = Seeker.objects.all()
        serializer = SeekerSerializer(
            seekers, many = True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None): 
        try: 

            seeker = Seeker.objects.get(pk=pk)
            serializer = SeekerSerializer(
                seeker, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)