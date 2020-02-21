from django.db import models

# Create your models here.
class UploadModel(models.Model):
    moviename=models.CharField(max_length=30)
    song=models.FileField(upload_to='songs/')
