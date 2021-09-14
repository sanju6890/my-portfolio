from django.contrib import admin
from .models import Project, Skill, Experience, Education, AboutMe
from django.contrib.auth.models import User, Group

# Header & Title Customization
admin.site.site_title = "Sanjay-Portfolio"
admin.site.site_header = "Sanjay Kumar's Portfolio"

# To Show the data in  tabular format on the admin-site
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','summary','url']

class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill','level']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title','company','type','summary']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['school_name','degree','session','courses', 'grade']

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['summary']

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(AboutMe, AboutMeAdmin)

# Unregister your models here.
admin.site.unregister(User)
admin.site.unregister(Group)