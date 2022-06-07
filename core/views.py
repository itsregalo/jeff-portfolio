from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from core.models import AboutMe, Education, MyTechStach, Portfolio, ProffessionalSkill, ProgrammingLanguage, Project, WorkExperience
from .views import *

from .forms import ContactForm

# Create your views here.


def IndexView(request):
    portfolio = Portfolio.objects.first()
    proffessional_skills = ProffessionalSkill.objects.all()
    languages = ProgrammingLanguage.objects.all()
    about_me = AboutMe.objects.first()
    education = Education.objects.all()
    work_experience = WorkExperience.objects.all()
    my_stack = MyTechStach.objects.all()
    projects = Project.objects.all()

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect(reverse('core:index'))
    context = {
        'portfolio': portfolio,
        'about_me': about_me,
        'proffessional_skills': proffessional_skills,
        'languages': languages,
        'about_me': about_me,
        'education': education,
        'work_experience': work_experience,
        'my_stack': my_stack,
        'projects': projects,
        'contact_form': contact_form

    }
    return render(request, 'index.html', context)