# Generated by Django 5.0.1 on 2024-01-17 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
    ]