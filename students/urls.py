from django.urls import path
from rest_framework import routers
from .views import SamplesListCreate,SampleRetrieveUpdateDestroy
from . import views

#router = routers.DefaultRouter()
#router.register('students',StudentsViewSet)

#urlpatterns =router.urls
urlpatterns = [
    path('samples/', SamplesListCreate.as_view()),
    path('samples/<int:pk>/',views.SampleRetrieveUpdateDestroy.as_view()),
   ]
