from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=False, null=False)
    occupation = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    registration_date = models.DateField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    overall_progress = models.FloatField()

    def __str__(self):
        return self.user
    