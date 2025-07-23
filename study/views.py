from django.shortcuts import render
from django.utils import timezone
from .models import *
from collections import defaultdict

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

    profile = request.user.profile
    subjects = Subject.objects.filter(profile=profile)


    context = {
        'subjects' : subjects,
    }
    return render(request, 'study/subjects.html', context)

def subject_view(request, name):
    subject = Subject.objects.get(name=name)
    context = {
        'subject' : subject
    }

    return render(request, 'subject_view.html', context)

def sessions(request):
    profile = request.user.profile
    all_sessions = StudySession.objects.filter(study_plan__profile=profile).order_by('start')

    scheduled_sessions = [s for s in all_sessions if s.status == 'scheduled']
    in_progress_sessions = [s for s in all_sessions if s.status == 'in_progress']
    completed_sessions = [s for s in all_sessions if s.status == 'completed']

    context = {
        'scheduled_sessions' : scheduled_sessions,
        'in_progress_sessions' : in_progress_sessions,
        'completed_sessions' : completed_sessions
    }
    # for plan in study_plans:
    #     plan.has_sessions = plan.sessions.exists()
    #     plan.ordered_sessions = plan.sessions.all().order_by('end')
    # context = {
    #     'study_plans':study_plans
    # }
    return render(request, 'study/sessions.html', context)

def study_plans(request):
    return render(request, 'study_plans.html', {})