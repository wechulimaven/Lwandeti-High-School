from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.boarding_students, name='boarding_students')
]