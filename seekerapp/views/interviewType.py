from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from rest_framework import serializers
from rest_framework import status
from seekerapp.models import InterviewType
class InterviewTypeSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = InterviewType
        url = serializers.HyperlinkedIdentityField(
            view_name='interviewTypes', 
            lookup_field='id'
        )
        fields = ('id', 'name') 
        depth = 1
class InterviewTypes(ViewSet): 
    def list(self, request): 
        interviewTypes = InterviewType.objects.all()
        serializer = InterviewTypeSerializer(
            interviewTypes, many = True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None): 
        try: 
            interviewTypes = InterviewTypes.objects.get(pk=pk)
            serializer = InterviewTypeSerializer(
                interviewTypes, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)