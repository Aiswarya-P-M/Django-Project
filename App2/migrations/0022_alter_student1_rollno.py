# Generated by Django 5.1.2 on 2024-10-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0021_alter_student1_teacher_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student1",
            name="rollno",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]