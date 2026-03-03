from django.db import models
import os

def file_save_path(instance, filename):
    return os.path.join('student/media/', instance.name, filename)

# Create your models here.
class Student(models. Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.TextField(max_length=150)
    password = models.CharField(max_length=15)
    checkbox = models.BooleanField(default=False)
    photo = models.FileField(upload_to=file_save_path, default=None, null=True)
    def __str__(self):
        return f"{self.name}"
