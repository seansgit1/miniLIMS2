from django.db import models

class material(models.Model):
    Name =models.CharField(max_length=100)
    Description = models.CharField(max_length=150)
    #CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name

class test(models.Model):
    Name =models.CharField(max_length=100)
    Description = models.CharField(max_length=150)
    #CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name

class event(models.Model):
    Name =models.CharField(max_length=100)
    Description = models.CharField(max_length=150)
    
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
    Material = models.ForeignKey(material,on_delete=models.CASCADE,null=True, blank=True)
    Status = models.ForeignKey(status,on_delete=models.CASCADE)
    Event = models.ForeignKey(event,on_delete=models.CASCADE,null=True, blank=True)
    #CreatedDt = models.DateTimeField(auto_now_add=True)
    UserText1 =models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        ordering = ['-Identifier']

    def __str__(self):
        return self.Identifier

class sample_result(models.Model):
    Sample = models.ForeignKey(sample,on_delete=models.CASCADE,null=False, blank=False)
    Test = models.ForeignKey(test,on_delete=models.CASCADE,null=False, blank=False)
    ValueNum = models.FloatField(null=True, blank=True)
    
    class Meta:
        ordering = ['Test']

    def __str__(self):
        return f"{self.Sample.Identifier} - {self.Test.Name}: {self.ValueNum}"
