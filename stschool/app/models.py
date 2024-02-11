from django.db import models
class Students(models.Model):
    الاسم = models.CharField(max_length=50)
    photo = models.FileField(upload_to="media/")
    tel = models.TextField()
    data = models.DateField()
    gender= models.TextField()
    mark = models.TextField()
    degree = models.TextField()
    الدفع = models.CharField(max_length=50)
    العنوان = models.TextField()




class FormConfiguration(models.Model):
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return "Form Configuration"
