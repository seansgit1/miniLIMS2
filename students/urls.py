from django.urls import path
from rest_framework import routers
from .views import SamplesListCreate, SampleRetrieveUpdateDestroy, StatusList, MaterialList, EventList, SampleResultList, SampleResultUpdate
from . import views

#router = routers.DefaultRouter()
#router.register('students',StudentsViewSet)

#urlpatterns =router.urls
urlpatterns = [
    path('samples/', SamplesListCreate.as_view()),
    path('samples/<int:pk>/',views.SampleRetrieveUpdateDestroy.as_view()),
    path('statuses/', StatusList.as_view()),
    path('materials/', MaterialList.as_view()),
    path('events/', EventList.as_view()),
    path('sample-results/<int:sample_id>/', SampleResultList.as_view()),
    path('sample-results/update/<int:pk>/', SampleResultUpdate.as_view()),
]
