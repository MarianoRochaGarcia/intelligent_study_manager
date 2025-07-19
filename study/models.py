from django.db import models
from accounts.models import Profile

class Subject(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.name

class StudyPlan(models.Model):

    STATUS_CHOICES = [
        ('scheduled', 'En progreso'),
        ('completed', 'Concluido'),
        ('missed', 'Fuera de tiempo'),
        ('cancelled', 'Cancelado')
    ]
    
    title = models.CharField(max_length=30, blank=False, null=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_date = models.DateField()
    limit_date = models.DateField()
    target_hours = models.IntegerField(blank=True, null=True)
    progress_hours = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15)

    def __str__(self):
        return self.title

class StudySession(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'En progreso'),
        ('completed', 'Concluido'),
        ('cancelled', 'Cancelado'),
    ]
    title = models.CharField(max_length=30)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    notes = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(choices = STATUS_CHOICES, max_length=15)

    def __str__(self):
        return self.title
