# Generated by Django 5.1.2 on 2024-10-25 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0020_alter_teacher_emp_id"),
        ("app_Teacher", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student1",
            name="teacher_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app_Teacher.teacher2",
            ),
        ),
    ]