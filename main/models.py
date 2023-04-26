from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default=None)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")