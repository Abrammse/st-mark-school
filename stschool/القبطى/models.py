from django.db import models
from ckeditor.fields import RichTextField
class القبطى1(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class القبطى11(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى12(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى13(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى2(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class القبطى21(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى22(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى23(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى3(models.Model):
    واصف1=RichTextField()
    صورة1=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    عنوان1 = RichTextField()
    واصف2=RichTextField()
    عنوان2=RichTextField()
    صورة2=models.FileField(upload_to="header/", max_length=250, null=True, default=None)
    واصف3=RichTextField()
    عنوان3=RichTextField()
    صورة3=models.FileField(upload_to="header/", max_length=250, null=True, default=None)

class القبطى31(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى32(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")

class القبطى33(models.Model):
    العنوان=   RichTextField()
    الواصف = RichTextField()
    pdf= models.FileField(upload_to="header/")
    audios= models.FileField(upload_to="header/")
