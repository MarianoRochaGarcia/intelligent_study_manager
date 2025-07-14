from django.db import models
from accounts.models import Profile

class Notification(models.Model):
    TYPE_CHOICES = [
        ('reminder', 'Recordatorio'),
        ('alert', 'Alerta'),
    ]

    title = models.CharField(max_length=15, blank=False, null=False, default='Notificacion')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.CharField(max_length=100, blank=False, null=False)
    reminder_time = models.DateTimeField()
    type = models.CharField(choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
    

