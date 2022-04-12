from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    is_cs = models.BooleanField()
    age = models.IntegerField()