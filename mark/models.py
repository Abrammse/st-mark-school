from django.db import models
class mark(models.Model):
    mark_sub=models.CharField(max_length=50)
    mark_title=models.CharField(max_length=200)
    mark_image = models.FileField(upload_to="header/", max_length=250, null=True, default=None)

# Create your models here.

def get_upload_path(instance, filename):
    return 'header/{}'.format(filename)

class YourModel(models.Model):
    mark_image = models.FileField(upload_to=get_upload_path, max_length=250, null=True, default=None)
    # Other fields in your model

    def __str__(self):
        return str(self.mark_image)