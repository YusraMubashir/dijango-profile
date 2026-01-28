from django.db import models

class Project(models.Model):  # Must be 'Project'
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)
    tech_used = models.CharField(max_length=200)

    def __str__(self):
        return self.title