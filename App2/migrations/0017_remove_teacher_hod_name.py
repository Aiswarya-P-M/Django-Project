# Generated by Django 5.1.2 on 2024-10-24 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0016_student1_created_on_student1_updated_on_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="hod_name",
        ),
    ]
