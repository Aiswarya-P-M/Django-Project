# Generated by Django 5.1.2 on 2024-10-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_School", "0003_remove_school_dept_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="sc_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
