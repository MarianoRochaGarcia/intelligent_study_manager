
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    path('subject_view/<str:name>', views.subject_view, name='subject_view'),
    path('subject_edit/<str:name>', views.subject_edit, name='subject_edit'),
    path('sessions/', views.sessions, name='sessions'),
    path('session/<str:title>', views.sessions, name='session_view'),
    path('study_plans/', views.study_plans, name='study_plans'),
    path('study_plan_view/<str:title>', views.study_plan_view, name='study_plan_view'),
    path('study_plan_edit/<str:title>', views.study_plan_edit, name="study_plan_edit"),
]
