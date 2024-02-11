from django.db import models
from ckeditor.fields import RichTextField

class الاخبار(models.Model):
    القسم=models.CharField(max_length=50)
    العنوان=models.CharField(max_length=50)
    الواصف =RichTextField()
    الصورة = models.FileField(upload_to="header/",max_length=250,null=True,default=None)

# Create your models here.


# Create your models here.
