from django.db import models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    meals_made = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.
