# Generated by Django 4.2.5 on 2023-09-14 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petproassist', '0002_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='user',
        ),
    ]
