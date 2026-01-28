from django.db import models

class Bio(models.Model):  # Make sure "Bio" is spelled exactly like this
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    description = models.TextField()

    def __str__(self):
        return self.name