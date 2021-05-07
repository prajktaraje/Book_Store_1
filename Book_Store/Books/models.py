from django.db import models

# Create your models here.
class Book(models.Model):
    Author=models.CharField(max_length=122,default='')
    Title=models.CharField(max_length=122,default='')
