from django.db import models
class الخدام(models.Model):
    اسمه = models.CharField(max_length=50)
    دوره = models.CharField(max_length=50)
    الصورة = models.FileField(upload_to="header/", max_length=250, null=True, default=None)

# Create your models here.
