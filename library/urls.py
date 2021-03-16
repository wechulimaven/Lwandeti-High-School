from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.all_asset, name = 'all_asset'),
    path('add/', views.add_asset, name = 'add_asset'),
]
