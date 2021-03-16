from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'teachers'
urlpatterns = [
    path('', views.login_teacher, name = 'login_teacher'),
    path('attribute/', views.teachers_profile_attribute, name='teachers_profile_attribute'),
    path('eddit_attribute/', views.edit_teachers_profile_attribute, name='edit_teachers_profile_attribute'),
    path('profile/', views.teacher_profile, name = 'teacher_profile'),
    path('my_profile/', views.stuff_profile, name = 'stuff_profile'),
    
    path('add_student_subject/', views.add_student_subject, name = 'add_student_subject'),
    path('add_student_subjects/<int:id>/', views.register_student_subject, name = 'register_student_subject'),
    
    path('student_subjects/', views.student_subjects, name = 'student_subjects'),
    path('students_attributes/', views.student_profile_attrib, name = 'students_attributes'),

    
    path('logout/', views.user_logout, name = 'user_logout'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)