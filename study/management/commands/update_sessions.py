from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from study.models import StudySession

class Command(BaseCommand):

    help = 'Actualiza el estado de las sesiones y elimina las sesiones viejas'
    
    def handle(self, *args, **options):
        now = timezone.now()

        sessions = StudySession.objects.filter()

        in_progress = 0
        finished = 0
        deleted = 0



        for session in sessions:
            # Check that no more than two days have passed  since the session
            if now > session.end:
                if now - session.end > timedelta(days=2):
                    session.delete()
                    deleted += 1
                elif session.status!='completed':
                    session.status = 'completed'
                    session.save()
                    finished += 1
            elif session.start < now < session.end and session.status == 'scheduled':
                session.status = 'in_progress'
                session.save()
                in_progress += 1
                
        self.stdout.write(self.style.SUCCESS(f'{in_progress} updated sessions to "in_progress"'))
        self.stdout.write(self.style.SUCCESS(f'{finished} updated sessions to "finished"'))
        self.stdout.write(self.style.SUCCESS(f'{deleted} deleted sessions due to age '))