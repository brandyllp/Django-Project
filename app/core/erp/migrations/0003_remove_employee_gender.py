# Generated by Django 3.1.4 on 2020-12-20 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_employee_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]
