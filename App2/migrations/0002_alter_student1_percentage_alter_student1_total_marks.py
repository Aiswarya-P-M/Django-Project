# Generated by Django 5.1.2 on 2024-10-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student1",
            name="percentage",
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name="student1",
            name="total_marks",
            field=models.FloatField(editable=False),
        ),
    ]
