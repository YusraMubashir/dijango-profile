from django.db import models

class Education(models.Model):  # Must be 'Education' with capital E
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    passing_year = models.IntegerField()
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.degree