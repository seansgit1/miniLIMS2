from django.urls import path
from rest_framework import routers
from .views import StudentsListCreate,StudentRetrieveUpdateDestroy,SamplesListCreate,SampleRetrieveUpdateDestroy
from . import views

#router = routers.DefaultRouter()
#router.register('students',StudentsViewSet)

#urlpatterns =router.urls
urlpatterns = [
    path('samples/', SamplesListCreate.as_view()),
    path('students/', StudentsListCreate.as_view()),
    path('students/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
    path('samples/<int:pk>/',views.SampleRetrieveUpdateDestroy.as_view()),
   ]
