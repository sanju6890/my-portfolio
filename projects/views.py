from django.shortcuts import render
from .models import Project, Skill, Experience

# Create your views here.
def home(request):
    projects = Project.objects
    skills = Skill.objects
    experiences = Experience.objects
    return render(request, 'projects/home.html', {'projects':projects, 'skills':skills, 'experiences':experiences})
