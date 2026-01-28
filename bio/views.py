from django.shortcuts import render
# We import all your models so the view can see them
from .models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def portfolio_home(request):
    # Fetching data from the database
    # .first() gets one person, .all() gets the whole list
    context = {
        'bio': Bio.objects.first(),
        'educations': Education.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
    }
    # This sends the 'context' dictionary to your HTML file
    return render(request, 'portfolio.html', context)
