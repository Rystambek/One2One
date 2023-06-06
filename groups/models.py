from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.name