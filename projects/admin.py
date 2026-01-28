from django.contrib import admin
from .models import Project  # This must match 'class Project' exactly

admin.site.register(Project)
