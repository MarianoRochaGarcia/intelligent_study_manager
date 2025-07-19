
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subjects, name='subjects'),
    path('subject/<str:name>', views.subjects, name='subject_view'),
    path('sessions/', views.sessions, name='sessions'),
    path('session/<str:title>', views.sessions, name='session_view'),
    path('study_plans/', views.study_plans, name='study_plans'),
    path('study_plans/<str:title>', views.study_plans, name='study_plans')

]
