from django.db import models

# Create your models here.

class Guidedetails(models.Model):
    Guidename = models.CharField(max_length=20)
    Phonenumber = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Places_To_Visit = models.CharField(max_length=500)
    Activities_To_Do = models.CharField(max_length=250)
    Duration = models.CharField(max_length=50)
    Transport_Details = models.CharField(max_length=100)
    Food_Details = models.CharField(max_length=100)
    Price = models.IntegerField()

