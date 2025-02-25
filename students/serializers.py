from rest_framework import serializers
from .models import sample,status,material,test,sample_result,event

class SampleSerializer(serializers.ModelSerializer):
    Status_Name = serializers.CharField(source='Status.Name', read_only=True)
    Material_Name = serializers.CharField(source='Material.Name', read_only=True)
    Event_Name = serializers.CharField(source='Event.Name', read_only=True)

    class Meta:
        model = sample
        fields = ['id','Identifier','Status','Status_Name','Material','Material_Name','Event','Event_Name','UserText1']    

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ['id', 'Name', 'Description']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = ['id', 'Name', 'Type']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = material
        fields = ['id', 'Name', 'Description']

class TestSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields =[',id', 'Name', 'Description']

class Sample_ResultSerializer(serializers.ModelSerializer):
    Test_Name = serializers.CharField(source='Test.Name', read_only=True)
    
    class Meta:
        model = sample_result
        fields = ['id', 'Sample', 'Test', 'Test_Name', 'ValueNum']