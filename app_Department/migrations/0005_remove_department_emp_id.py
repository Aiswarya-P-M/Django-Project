# Generated by Django 5.1.2 on 2024-10-24 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_Department", "0004_alter_department_emp_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="department",
            name="emp_id",
        ),
    ]