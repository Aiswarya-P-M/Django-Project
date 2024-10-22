# import os
# import django
# # Set the Django settings module (replace with your project's settings)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# # Initialize Django
# django.setup()

from App2.models import *  # Import your models
from App2.utils import *

def update_teacher_performance():
    teachers = Teacher.objects.all()  # Fetch all teachers

    for teacher in teachers:
        teacher_id = teacher.emp_id   # Assuming 'emp_id' is the field used for teacher identification
        pass_percentage = calculate_teacher_pass_percentage(teacher_id)

        # Update the performance field for the teacher
        teacher.performance = pass_percentage
        teacher.save()  # Save the updated performance in the database

    print("Teacher performance updated successfully.")

def run():
    print("Updating teacher performance...")
    update_teacher_performance()

if __name__ == "__main__":
    run()

