from django.db import models

# Create your models here.

 class Slider(models.Model):

     heading = models.CharField()

     description = models.CharField()

     image = models.ImageField()


 class Vision(models.Model):

     pass


 class Events(models.Model):

     pass


 class