from django.urls import path
from teachers import views as teachers_views
from subjects import views as subjects_views
from library import views as library_views
from staff import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'staff'
urlpatterns = [
    path('', teachers_views.add_teachers_profile, name = 'add_teachers_profile'),
    path('teacher_attribute/', teachers_views.teachers_profile_attribute, name = 'teachers_profile_attribute'),
    path('student_admission/', views.add_student, name = 'add_student'),
    path('all_teachers/', views.all_teachers, name = 'all_teachers'),

    path('all_student/', views.all_student, name='all_students'),
    path('<category_slug>', views.all_student, name='all_student_url'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('assign_hostel/', views.assign_hostel, name='assign_hostel'),
    
    path('add_subject/', subjects_views.add_subject, name='add_subject'),
    path('add_asset/', library_views.add_asset, name='add_asset'),
    path('all_assets/', library_views.all_asset, name = 'all_asset'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)