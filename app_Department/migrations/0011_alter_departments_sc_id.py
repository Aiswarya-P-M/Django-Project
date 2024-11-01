# Generated by Django 5.1.2 on 2024-10-30 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_Department", "0010_departments_is_active"),
        ("app_School", "0005_school_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="departments",
            name="sc_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="school_departments",
                to="app_School.school",
            ),
        ),
    ]
