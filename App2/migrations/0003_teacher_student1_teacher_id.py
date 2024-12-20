# Generated by Django 5.1.2 on 2024-10-22 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0002_alter_student1_percentage_alter_student1_total_marks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("emp_id", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name="student1",
            name="teacher_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="App2.teacher",
            ),
        ),
    ]
