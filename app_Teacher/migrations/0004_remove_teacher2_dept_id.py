# Generated by Django 5.1.2 on 2024-10-30 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_Teacher", "0003_teacher2_department"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher2",
            name="dept_id",
        ),
    ]