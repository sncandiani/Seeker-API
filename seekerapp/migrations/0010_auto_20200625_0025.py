# Generated by Django 3.0.7 on 2020-06-25 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekerapp', '0009_application_seeker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='created_at',
        ),
        migrations.AddField(
            model_name='application',
            name='applicationDate',
            field=models.DateTimeField(null=True),
        ),
    ]
