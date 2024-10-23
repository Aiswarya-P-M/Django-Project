from App2.models import *  
from App2.utils import *


def datafetch():

    # Fetch all teacher employee IDs
    teacher_ids = Teacher.objects.values_list('emp_id', flat=True)
    print("Teacher IDs:", list(teacher_ids))

    # Fetch all students
    students = Student1.objects.all()

    # Iterate through all students
    for student in students:
        try:
            # Get the teacher based on the student's teacher ID
            if student.teacher_id in teacher_ids:  # Ensure the teacher exists
                teacher = Teacher.objects.get(emp_id=student.teacher_id)
                student.teacher_id = teacher  # Assign the teacher to the student
                student.save()  # Save the changes

                # Print confirmation for each student update
                print(f"Updated student ID {student.name} ({student.name}) with teacher ID {teacher.emp_id} ({teacher.name})")
            else:
                print(f"No matching teacher ID {student.teacher_id} for student ID {student.name} ({student.name}).")
        except Teacher.DoesNotExist:
            print(f"Teacher with ID {student.teacher_id} does not exist for student ID {student.name} ({student.name}).")
        except Exception as e:
            print(f"An error occurred while updating student ID {student.name}: {e}")

def update_teacher_performance():
    teachers=Teacher.objects.all()
    for teacher in teachers:
        try:
            pass_percentage=calculate_teacher_pass_percentage(teacher.emp_id)
            teacher.performance=pass_percentage
            teacher.save()
            print(f"Updated performance for Teacher ID {teacher.emp_id} ({teacher.name}) to {teacher.performance}%")
        except Exception as e:
            print(f"An error occurred while updating performance for Teacher ID {teacher.emp_id}: {e}")

def run():
    print("Fetching the data")
    datafetch()
    print("Updating teacher performance...")
    update_teacher_performance()
 
if __name__ == "__main__":
    run()
 
