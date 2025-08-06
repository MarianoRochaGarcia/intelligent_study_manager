from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudySession
from django.core.management import call_command

@receiver(post_save, sender = StudySession)
def update_session_after_creation(sender, instance, created, **kwargs):
    if created:
        call_command('update_sessions')