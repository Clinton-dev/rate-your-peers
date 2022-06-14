from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(null=False, max_length=150)
    description = models.CharField(null=False, max_length=200)
    link = models.CharField(null=False, max_length=200)
    image = models.ImageField(default='default.jpg', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} project'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})


class Rating(models.Model):
    design = models.IntegerField(default=0, blank=True)
    usability = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(10)],blank=True)
    content = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)