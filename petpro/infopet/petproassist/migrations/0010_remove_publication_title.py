# Generated by Django 4.2.5 on 2023-09-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petproassist', '0009_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='title',
        ),
    ]