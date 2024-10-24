# Generated by Django 5.1.2 on 2024-10-24 04:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_Department", "0002_department_created_on_department_updated_on"),
        ("app_School", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="school",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="school",
            name="dept_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app_Department.department",
            ),
        ),
        migrations.AddField(
            model_name="school",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
