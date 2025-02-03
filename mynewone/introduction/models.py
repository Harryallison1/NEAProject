from django.db import models

# Create your models here.

class Questions(models.Model):
    specification = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

#class Answers(models.Model):
    