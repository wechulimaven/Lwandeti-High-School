from django.db import models
from subjects.models import Subject
# Create your models here.

class LibraryAsset(models.Model):
    title = models.CharField(max_length = 191)
    author_name = models.CharField(max_length = 191)
    publisher = models.CharField(max_length = 191)
    subject = models.CharField(max_length = 191)
    department = models.CharField(max_length = 191)
    asset_type = models.CharField(max_length = 191)
    status = models.CharField(max_length = 191)
    purchase_date = models.CharField(max_length = 191)
    price = models.CharField(max_length = 191)
    asset_details = models.TextField(max_length = 191)
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.title} : {self.subject}'