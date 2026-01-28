from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency_percentage = models.IntegerField() # Enter a number like 80 or 90

    def __str__(self):
        return self.name
