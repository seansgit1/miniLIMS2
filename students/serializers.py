from rest_framework import serializers
from .models import student,sample

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id','name','course','rating']    


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = sample
        fields = ['id','Identifier','Status','UserText1']    
