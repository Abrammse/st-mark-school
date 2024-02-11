from django.db import models
from ckeditor.fields import RichTextField
class اللحان1(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class اللحان11(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان12(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان13(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان2(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class اللحان21(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان22(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان23(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان3(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class اللحان31(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان32(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class اللحان33(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")
