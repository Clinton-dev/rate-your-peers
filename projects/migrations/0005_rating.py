# Generated by Django 4.0.5 on 2022-06-13 11:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usability', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('content', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('score', models.FloatField(blank=True, default=0)),
                ('design_average', models.FloatField(blank=True, default=0)),
                ('usability_average', models.FloatField(blank=True, default=0)),
                ('content_average', models.FloatField(blank=True, default=0)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
