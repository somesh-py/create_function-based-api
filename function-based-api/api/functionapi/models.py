from django.db import models

# Create your models here.


class Employee(models.Model):
    eno=models.IntegerField()
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    active=models.BooleanField()
    address=models.CharField(max_length=50)