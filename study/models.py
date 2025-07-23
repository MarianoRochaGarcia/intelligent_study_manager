from django.db import models
from accounts.models import Profile

class Subject(models.Model):

    SUBJECT_COLORS  = [
        ('green', 'Verde'),
        ('lime', 'Limon'),
        ('teal', 'Turquesa'),
        ('blue', 'Azul'),
        ('violet', 'Violeta'),
        ('purple', 'Morado'),
        ('wine', 'Vino'),
        ('red', 'Rojo'),
        ('tangerine', 'Mandarina'),
        ('orange', 'Naranja'),
        ('yellow', 'Amarillo')
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=False, null=False)
    teacher = models.CharField(max_length=50, blank=True, null=True, default='Sin asignar')
    description = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(blank=False, null=False, choices=SUBJECT_COLORS)

    def get_color_classes(self):
        color_map = {
            'green': 'bg-green-100 text-green-800',
            'lime': 'bg-lime-100 text-lime-800',
            'teal': 'bg-teal-100 text-teal-800',
            'blue': 'bg-blue-100 text-blue-800',
            'violet': 'bg-violet-100 text-violet-800',
            'purple': 'bg-purple-100 text-purple-800',
            'red': 'bg-red-100 text-red-800',
            'orange': 'bg-orange-100 text-orange-800',
            'yellow': 'bg-yellow-100 text-yellow-800',
        }
        return color_map.get(self.color)

    def get_bg_classes(self):
        color_map = {
            'green': 'bg-green-100',
            'lime': 'bg-lime-100',
            'teal': 'bg-teal-100',
            'blue': 'bg-blue-100',
            'violet': 'bg-violet-100',
            'purple': 'bg-purple-100',
            'red': 'bg-red-100',
            'orange': 'bg-orange-100',
            'yellow': 'bg-yellow-100',
        }
        return color_map.get(self.color)
     
    def get_text_classes(self):
        color_map = {
            'green': 'text-green-800',
            'lime': 'text-lime-800',
            'teal': 'text-teal-800',
            'blue': 'text-blue-800',
            'violet': 'text-violet-800',
            'purple': 'text-purple-800',
            'red': 'text-red-800',
            'orange': 'text-orange-800',
            'yellow': 'text-yellow-800',
        }
        return color_map.get(self.color)

    def __str__(self):
        return self.name
    
class ClassSchedule(models.Model):

    DAYS_OF_WEEK = [
        ('MO','Lunes'),
        ('TU', 'Martes'),
        ('WE', 'Miercoles'),
        ('TH', 'Jueves'),
        ('FR', 'Viernes'),
        ('SA', 'Sabado'),
        ('SU', 'Domingo'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=2, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_display()} {self.start_time}-{self.end_time}"


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
        ('scheduled', 'Programada'),
        ('in_progress', 'En progreso'),
        ('completed', 'Completada'),
    ]
    title = models.CharField(max_length=30)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE, related_name='sessions')
    start = models.DateTimeField()
    end = models.DateTimeField()
    notes = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(choices = STATUS_CHOICES, max_length=15)

    def get_color_status(self):
        color_map = {
            'scheduled': 'bg-blue-100 text-blue-800',
            'in_progress': 'bg-yellow-100 text-yellow-800',
            'completed': 'bg-green-100 text-green-800',
        }
        return color_map.get(self.status)
    
    def get_bg_status(self):
        color_map = {
            'scheduled': 'bg-blue-100',
            'in_progress': 'bg-yellow-100',
            'completed': 'bg-green-100',
        }
        return color_map.get(self.status)
    
    def get_text_status(self):
        color_map = {
            'scheduled': 'text-blue-800',
            'in_progress': 'text-yellow-800',
            'completed': 'text-green-800',
        }
        return color_map.get(self.status)

    def __str__(self):
        return self.title
