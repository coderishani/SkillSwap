from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile" \
    "profile")
    bio=models.TextField(max_length=500, blank=True)
    skills_can_teach=models.TextField(max_length=500, blank=True)
    skills_to_learn=models.TextField(max_length=500, blank=True)

# Create your models here.
