from django.contrib import admin
from staff.models import Designation,TeachersProfileAttrib,ClassTeacherProfile, StudentProfileAttribute, StudentSubjects
from students.models import Formclass
class FormClassAdmin(admin.ModelAdmin):
    list_display = ['form_name', 'slug', 'class_rep', 'class_logo']
    prepopulated_fields = {'slug': ('form_name',)}
    
admin.site.register(Formclass, FormClassAdmin)
admin.site.register(Designation)
admin.site.register(TeachersProfileAttrib)
admin.site.register(ClassTeacherProfile)
admin.site.register(StudentProfileAttribute)
admin.site.register(StudentSubjects)


# Register your models here.
