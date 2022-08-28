from django.db import models

class patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password =models.IntegerField()


# Create your models here.
