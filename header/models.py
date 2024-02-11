from django.db import models
from ckeditor.fields import RichTextField

class header(models.Model):
    header_sub = models.CharField(max_length=50)
    header_title = models.CharField(max_length=50)
    header_des = models.TextField()
    header_des2 = models.TextField()
    header_image = models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    header_image2 = models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    header_image3 = models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    header_pr = models.FileField(upload_to="header/")






# Create your models here.
