# Generated by Django 5.1.2 on 2024-10-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0019_remove_teacher_hod_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="emp_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
