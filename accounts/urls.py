
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
]
