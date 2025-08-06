
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    path('subject_create/', views.subject_create, name='subject_create'),
    path('subject_view/<str:name>', views.subject_view, name='subject_view'),
    path('subject_edit/<str:name>', views.subject_edit, name='subject_edit'),
    path('subject_delete/<str:name>', views.subject_delete, name='subject_delete'),
    path('sessions/', views.sessions, name='sessions'),
    path('session_create/', views.session_create, name='session_create'),
    path('session_view/<str:title>', views.session_view, name='session_view'),
    path('session_edit/<str:title>', views.session_edit, name='session_edit'),
    path('session_delete/<str:title>', views.session_delete, name='session_delete'),
    path('study_plans/', views.study_plans, name='study_plans'),
    path('study_plan_create/', views.study_plan_create, name='study_plan_create'),
    path('study_plan_view/<str:title>', views.study_plan_view, name='study_plan_view'),
    path('study_plan_edit/<str:title>', views.study_plan_edit, name="study_plan_edit"),
    path('study_plan_delete/<str:title>', views.study_plan_delete, name="study_plan_delete"),
]
