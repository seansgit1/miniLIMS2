from django.shortcuts import render
from .models import sample, sample_result, status, material,event
from rest_framework.viewsets import ModelViewSet
from .serializers import SampleSerializer, StatusSerializer, MaterialSerializer,EventSerializer, Sample_ResultSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class SamplesListCreate(generics.ListCreateAPIView):
    serializer_class = SampleSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        #return Todo.objects.filter(user=user,datecompleted__isnull=True )
        return sample.objects.all()
    
    def perform_create(self,serializer):
        #user = User.objects.get(pk=1)
        #serializer.save(user=self.request.user)
        serializer.save()
   
class ResultsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #serializer_class =TodoSerializer 
    #permission_classes= [permissions.IsAuthenticated]
    serializer_class = Sample_ResultSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        return sample_result.objects.all()


class SampleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #serializer_class =TodoSerializer 
    #permission_classes= [permissions.IsAuthenticated]
    serializer_class = SampleSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        return sample.objects.all()

class StatusList(generics.ListAPIView):
    serializer_class = StatusSerializer
    permission_classes = [permissions.AllowAny]
    queryset = status.objects.all()

class MaterialList(generics.ListAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [permissions.AllowAny]
    queryset = material.objects.all()

class EventList(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    queryset = event.objects.all()

class SampleResultList(generics.ListAPIView):
    serializer_class = Sample_ResultSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        sample_id = self.kwargs['sample_id']
        return sample_result.objects.filter(Sample_id=sample_id)

class SampleResultUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Sample_ResultSerializer
    permission_classes = [permissions.AllowAny]
    queryset = sample_result.objects.all()
