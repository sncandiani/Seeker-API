# Generated by Django 3.0.7 on 2020-06-12 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seekerapp', '0002_company_isdeleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='isDeleted',
        ),
    ]