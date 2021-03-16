from django.contrib import admin
from .models import Subject, SubjectSyllabus, SubjectObjective, CompulsorySubjects

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'subject_code', 'subject_photo',]
    prepopulated_fields = {'subject_code': ('subject_name',)}
    
admin.site.register(Subject,SubjectAdmin)
admin.site.register(SubjectSyllabus)
admin.site.register(SubjectObjective)
admin.site.register(CompulsorySubjects)
