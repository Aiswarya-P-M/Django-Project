# Generated by Django 5.1.2 on 2024-10-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0004_remove_student1_classteacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="student1",
            name="classteacher",
            field=models.CharField(max_length=50, null=True),
        ),
    ]