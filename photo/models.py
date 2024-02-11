from django.db import models
from ckeditor.fields import RichTextField

class الصور(models.Model):
    الكلمة = RichTextField()
    عدد = models.CharField(max_length=50)
    التاريخ = models.DateField()
    المناسبة = RichTextField()





class الصورة(models.Model):
    الصورة = models.ImageField(upload_to='images/', blank=True)
    الصور = models.ForeignKey(الصور, related_name='الصور_الصورة', on_delete=models.CASCADE)
