# Generated by Django 5.1.2 on 2024-10-23 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0010_teacher_performance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student1",
            name="teacher_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="students",
                to="App2.teacher",
            ),
        ),
    ]