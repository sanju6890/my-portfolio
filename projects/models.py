from django.db import models

# Create your models here.
class AboutMe(models.Model):
    summary = models.TextField()
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    summary = models.TextField()
    url = models.URLField()

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=50)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    summary = models.TextField()

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    session = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
