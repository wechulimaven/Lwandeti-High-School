from django.db import models
from django.contrib.auth.models import User



class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 191, blank=True, null=True)
    last_name = models.CharField(max_length =191 , blank=True, null=True)
    id_number = models.CharField(max_length = 10, blank=True, null=True)
    
       

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class EducationStatus(models.Model):
    status_name = models.CharField(max_length = 191, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'EducationStatus'
    
    def __str__(self):
        return f'{self.status_name}'
    

    


