from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=30, unique=True)
    email=models.EmailField(unique=True)
# If you want to see the entries by peoples name then write this function.  

    def __str__(self):
        return f"{self.username} ({self.email})"
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    filename = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)