from django.db import models
from students.models import Formclass

class Subject(models.Model):
    formclass = models.ForeignKey(Formclass, on_delete = models.CASCADE, null=True, blank=True)
    subject_name = models.CharField(max_length = 191)
    subject_code = models.CharField(max_length = 191)
    # subject_hod = models.CharField(max_length = 191)
    
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    # department = models.CharField(max_length = 191)
    # subject_students_number = models.CharField(max_length = 191)
    # subject_students_number = models.ForeignKey(HodProfile, on_delete=models.CASCADE)
    # subject_details = models.TextField()
    subject_photo = models.ImageField(upload_to='subjects')    
    timestamp = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f'{self.subject_name}'
    
class CompulsorySubjects(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'CompulsorySubjects'
    
    def __str__(self):
        return f'{self.subject}'

class SubjectSyllabus(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    syllabus = models.TextField()

    def __str__(self):
        return f'{self.subject}: {self.syllabus}'

class SubjectObjective(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    objective = models.TextField()

    def __str__(self):
        return f'{self.subject}: {self.objective}'

