from django.shortcuts import render
from .models import student,sample
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer,SampleSerializer
from rest_framework import generics,permissions
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class SamplesListCreate(generics.ListCreateAPIView):
    serializer_class =SampleSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        #return Todo.objects.filter(user=user,datecompleted__isnull=True )
        return sample.objects.all()
    
    def perform_create(self,serializer):
        #user = User.objects.get(pk=1)
        #serializer.save(user=self.request.user)
        serializer.save()
   

class SampleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #serializer_class =TodoSerializer 
    #permission_classes= [permissions.IsAuthenticated]
    serializer_class =SampleSerializer
    permission_classes= [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        return sample.objects.all()