from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    occupation = models.CharField(max_length=30, blank=False, null=False)
    registration_date = models.DateField()

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    overall_progress = models.FloatField()

    def __str__(self):
        return self.user
    