from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    ingrediants = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
