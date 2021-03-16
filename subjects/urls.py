from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'subjects'
urlpatterns = [
    path('', views.all_subject, name = 'all_subject'),
    path('add/', views.add_subject, name = 'add_subject'),
    path('subject/<int:id>/', views.subject_detail, name = 'subject_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)