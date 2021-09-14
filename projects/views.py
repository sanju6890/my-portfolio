from django.shortcuts import render
from .models import Project, Skill, Experience, Education, AboutMe

# Create your views here.
def home(request):
    projects = Project.objects
    skills = Skill.objects
    experiences = Experience.objects
    education = Education.objects
    about = AboutMe.objects
    return render(request, 'projects/home.html', {'projects':projects, 'skills':skills, 'experiences':experiences, 'education':education, 'about':about})
