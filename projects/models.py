from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    url = models.URLField()

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=50)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
