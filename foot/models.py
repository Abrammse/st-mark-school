from django.db import models
class foot(models.Model):
    foot_sub = models.CharField(max_length=200)
    foot_title = models.CharField(max_length=200)

