from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import *

def index(request):

    now = timezone.now()

    profile = request.user.profile
    subjects = Subject.objects.filter(profile=profile)
    study_plans = StudyPlan.objects.filter(profile=profile)
    study_sessions = StudySession.objects.filter(study_plan__profile=profile)
    next_session = StudySession.objects.filter(study_plan__profile=profile, start__gt=now).order_by('start').first()
    context = {
        'profile' : profile,
        'subjects': subjects,
        'study_plans': study_plans,
        'study_sessions': study_sessions,
        'next_session' : next_session,
    }
    return render(request, 'index.html', context)

def subjects(request):
    return render(request, 'study/subject.html', {})

def sessions(request):
    return render(request, 'study/sessions.html', {})

def study_plans(request):
    return render(request, 'study_plans.html', {})