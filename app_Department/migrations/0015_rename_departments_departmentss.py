# Generated by Django 5.1.2 on 2024-11-06 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App2", "0025_remove_student1_chemistry_remove_student1_maths_and_more"),
        ("app_Department", "0014_remove_departments_sc_id"),
        ("app_School", "0008_alter_school_departments"),
        ("app_Teacher", "0004_remove_teacher2_dept_id"),
        ("app_User", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Departments",
            new_name="Departmentss",
        ),
    ]