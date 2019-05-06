from django.db import models

# Create your models here.

# models.py
from django.db import models


class Test(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    hotelId = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    star = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.CharField(max_length=1000)
    x = models.CharField(max_length=1000)
    y = models.CharField(max_length=1000)

class Tourism(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    tourismId = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.CharField(max_length=1000)
    x = models.CharField(max_length=1000)
    y = models.CharField(max_length=1000)

