# Generated by Django 4.0.5 on 2022-06-12 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created',
        ),
    ]
