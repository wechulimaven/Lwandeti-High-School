from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
#

HOSTEL_CHOICES = [
    ('H', 'Harambee'),
    ('Ch', 'Chesoni'),
    ('K', 'Kenya'),
    ('N', 'Nyayo'),
]

class Hostels(models.Model):
    hostel_name = models.CharField(max_length=191)
    slug = models.SlugField(max_length=200, db_index=True, default='inzu')
    hostel_logo = models.ImageField(upload_to = 'hostel_logo', null=True)
    
    def get_absolute_url(self):
        return reverse('students:boarding_student_url',
                       args=[self.slug])
    
    class Meta:
        verbose_name_plural = 'Hostels'
    
    def __str__(self):
        return f'{self.hostel_name}'
    
class Formclass(models.Model):
    form_name = models.CharField(max_length = 191)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    class_rep = models.CharField(max_length = 100, default = 'Principal')
    class_logo = models.ImageField(upload_to='class_logo', null = True)    
    class Meta:
        verbose_name_plural = 'formclasses' 
        
    def get_absolute_url(self):
        return reverse('staff:all_student_url',
                       args=[self.slug])   

    def __str__(self):
        return f'{self.form_name}' 

class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank=True)
    first_name = models.CharField(max_length = 191)
    last_name = models.CharField(max_length = 191)
    admission_number = models.CharField(max_length = 191)
    form_name = models.ForeignKey(Formclass, on_delete=models.CASCADE, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now = True) 
    gender = models.CharField(max_length=191)
    boarding = models.BooleanField(blank=False, default=False)    
    parent_name = models.CharField(max_length = 191, blank=False, null=False)
    parent_mobile_number = models.CharField(max_length = 191, blank=False, null=False)
    dob = models.CharField(max_length = 191)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    student_photo = models.ImageField(upload_to='student_picture')
    timestamp = models.DateTimeField(auto_now = True)
    
    # def Boarding(self):
    #     if self.boarding == True:
    #         return redirect("student:bording_student")
    #     else:
    #         return redirect("staff:add_student")

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.admission_number} {self.boarding}'
    
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_completed = models.BooleanField(blank=False, default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.student} {self.is_completed}'
    
class StudentBoarding(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    # hostel_name = models.CharField(choices=HOSTEL_CHOICES, max_length=2)
    hostel = models.ForeignKey(Hostels, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.student} : {self.hostel}'

    





    

