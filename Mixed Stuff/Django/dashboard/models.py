from django.db import models
import csv
from django.contrib.auth.models import User
# Create your models here.


class Infoklasse(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Prodcheck(models.Model):
    Typ = models.CharField(max_length = 200)
    DetailInfo = models.TextField()
    EventDay = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Typ


