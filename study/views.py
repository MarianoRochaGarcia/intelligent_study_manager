from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.contrib import messages
from .forms import SubjectForm, StudyPlanForm
from django.shortcuts import redirect

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

    return render(request, 'study/subject_view.html', context)

def subject_edit(request, name):

    subject = Subject.objects.get(name=name)
    if request.method == 'GET':
        form = SubjectForm(instance=subject)
        context = {
            'subject': subject,
            'form': form,
            'name': name
        }
        return render(request, 'study/subject_edit.html', context)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
           subject = form.save()
           messages.success(request, 'Materia actualizada correctamente')
           return redirect('subject_view', name=subject.name)

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

    return render(request, 'study/sessions.html', context)

def study_plans(request):
    profile = request.user.profile
    study_plans = StudyPlan.objects.filter(profile=profile)
    context = {
        'study_plans': study_plans
    }
    return render(request, 'study/study_plans.html', context)

def study_plan_view(request, title):
    study_plan = StudyPlan.objects.get(title=title)
    context = {
        'study_plan': study_plan
    }

    return render(request, 'study/study_plan_view.html', context)

def study_plan_edit(request, title):

    study_plan = StudyPlan.objects.get(title=title)
    if request.method == "GET":
        form = StudyPlanForm(instance=study_plan)
        context = {
            'study_plan' : study_plan,
            'form' : form,
            'title' : title
        }
        return render(request, 'study/study_plan_edit.html', context)
    if request.method == "POST":
        form = StudyPlanForm(request.POST, instance=study_plan)
        if form.is_valid():
            study_plan = form.save()
            return redirect('study_plan_view', title = study_plan.title)
