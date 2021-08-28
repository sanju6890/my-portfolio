from django.contrib import admin
from .models import Project, Skill, Experience

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

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)