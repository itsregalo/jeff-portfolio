from django.shortcuts import render

from core.models import AboutMe, Education, MyTechStach, Portfolio, ProffessionalSkill, ProgrammingLanguage, WorkExperience
from .views import *

# Create your views here.


def IndexView(request):
    portfolio = Portfolio.objects.first()
    proffessional_skills = ProffessionalSkill.objects.all()
    languages = ProgrammingLanguage.objects.all()
    about_me = AboutMe.objects.first()
    education = Education.objects.all()
    work_experience = WorkExperience.objects.all()
    my_stack = MyTechStach.objects.all()

    context = {
        'portfolio': portfolio,
        'about_me': about_me,
        'proffessional_skills': proffessional_skills,
        'languages': languages,
        'about_me': about_me,
        'education': education,
        'work_experience': work_experience,
        'my_stack': my_stack,
    }
    return render(request, 'index.html', context)