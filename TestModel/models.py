# models.py
from django.db import models


class Test(models.Model):
    url = models.CharField(max_length=500, default='')
    description = models.CharField(max_length=500, default='')
    click = models.IntegerField(default=0, verbose_name="点击次数")
