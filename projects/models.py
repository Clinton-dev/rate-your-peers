from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(null=False, max_length=150)
    description = models.CharField(null=False, max_length=200)
    link = models.CharField(null=False, max_length=200)
    image = models.ImageField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} project'