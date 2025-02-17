from django.db import models

class student(models.Model):
    name =models.CharField(max_length=140)
    course =models.CharField(max_length=140)
    rating =models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']

class material(models.Model):
    Name =models.CharField(max_length=100)
    Description = models.CharField(max_length=150)
    #CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name
    
class status(models.Model):
    Name =models.CharField(max_length=100)
    Type =models.IntegerField() 
    #CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name

class sample(models.Model):
    Identifier =models.CharField(max_length=100,null=True, blank=True)
    #SampleType = models.ForeignKey(SampleType,on_delete=models.CASCADE,null=True, blank=True)
    #SampleDt =models.DateTimeField(auto_now_add=True)
    #Priority = models.BooleanField(default=False)
    #Material = models.ForeignKey(material,on_delete=models.CASCADE,null=True, blank=True)
    Status = models.ForeignKey(status,on_delete=models.CASCADE)
    #Event = models.ForeignKey(Event,on_delete=models.CASCADE)
    #CreatedDt = models.DateTimeField(auto_now_add=True)
    UserText1 =models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        ordering = ['-Identifier']

    def __str__(self):
        return self.Identifier

    

