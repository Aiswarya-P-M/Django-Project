# Generated by Django 5.1.2 on 2024-11-05 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_Department", "0014_remove_departments_sc_id"),
        ("app_School", "0008_alter_school_departments"),
        ("app_User", "0005_alter_users_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="department",
            field=models.ManyToManyField(
                related_name="user_teacher_list", to="app_Department.departments"
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="first_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="users",
            name="last_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="users",
            name="performance",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="users",
            name="role",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="sc_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app_School.school",
            ),
        ),
    ]
