from django.db import models

# Create your models here.

from django.db import models


class person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phonenum = models.IntegerField()
    city = models.CharField(max_length=10)
    service = models.CharField(max_length=50)
    feedback = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pics")

