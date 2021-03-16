from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from teachers.models import TeacherProfile
from students.models import Student,Formclass
from subjects.models import Subject,CompulsorySubjects


class Designation(models.Model):
    desg_name = models.CharField(max_length = 191, blank=True, null=True)   
    def __str__(self):
        return f'{self.desg_name}' 
# class EducationStatus(models.Model):        

    
class ClassTeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    formclass = models.ForeignKey(Formclass, on_delete = models.CASCADE)
    # formclass = models.CharField(max_length = 191)
    year = models.CharField(max_length = 191)
    # students = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} :{self.formclass}'     
    
class TeachersProfileAttrib(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length = 191, blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 191, blank=True, null=True, default='Male')
    # email = models.EmailField()
    dob = models.CharField(max_length = 191, blank=True, null=True)
    address = models.CharField(max_length = 191, blank=True)
    educational_status = models.CharField(max_length = 191, blank=True)
    timestamp = models.DateTimeField(auto_now = True)    
    profile_photo = models.ImageField(upload_to='teacher_profile')
    joined_date = models.CharField(max_length = 191, blank=True, null=True)

    def __str__(self):
        return f'{self.teacher} : {self.designation} {self.educational_status}'
    
class StudentProfileAttribute(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classteacher = models.ForeignKey(ClassTeacherProfile, on_delete=models.CASCADE)
    formclass = models.CharField(max_length = 191, null=True, blank=True)
    session = models.CharField(max_length = 191)
    year = models.CharField(max_length = 191)
    
    def __str__(self):
        return f'{self.student} {self.classteacher}'
    
class StudentSubjects(models.Model):
    classteacher = models.ForeignKey(ClassTeacherProfile, on_delete = models.CASCADE, null=True, blank=True) #where supposed to be in clasteacher else create classteacherprofile 
    student = models.ForeignKey(StudentProfileAttribute, on_delete=models.CASCADE)
    # compulsory_subjects = models.ForeignKey(CompulsorySubjects, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.student} : {self.subjects}"

# class Formclass(models.Model):
#     form_name', 'slug', 'class_rep', 'class_logo
#     formName = models.CharField(max_length = 191, null=True, blank=True)
#     slug = models.slu
