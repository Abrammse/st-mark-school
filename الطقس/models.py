from django.db import models
from ckeditor.fields import RichTextField
class الطقس1(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class الطقس11(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس12(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس13(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس2(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class الطقس21(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس22(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس23(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس3(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class الطقس31(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس32(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class الطقس33(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")
