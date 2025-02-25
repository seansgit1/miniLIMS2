from doctest import testmod
from django.contrib import admin
from .models import sample,material,status, sample_result,test,event


admin.site.register(sample)
admin.site.register(material)
admin.site.register(status)
admin.site.register(sample_result)
admin.site.register(test)
admin.site.register(event)
