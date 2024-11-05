from App2.models import Student1
from app_Teacher.models import Teacher2 
from App2.utils import calculate_teacher_pass_percentage
from app_School.models import School
from app_Department.models import Departments
from django.utils.crypto import get_random_string
from app_User.models import Users
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import random
import string

def datafetch():

    # Fetch all teacher employee IDs
    teacher_ids = Teacher2.objects.values_list('emp_id', flat=True)
    print("Teacher IDs:", list(teacher_ids))

    # Fetch all students
    students = Student1.objects.all()

    # Iterate through all students
    for student in students:
        try:
            # Get the teacher based on the student's teacher ID
            if student.teacher_id in teacher_ids:  # Ensure the teacher exists
                teacher = Teacher2.objects.get(emp_id=student.teacher_id)
                student.teacher_id = teacher  # Assign the teacher to the student
                student.save()  # Save the changes

                # Print confirmation for each student update
                print(f"Updated student ID {student.name} ({student.name}) with teacher ID {teacher.emp_id} ({teacher.name})")
            else:
                print(f"No matching teacher ID {student.teacher_id} for student ID {student.name} ({student.name}).")
        except Teacher2.DoesNotExist:
            print(f"Teacher with ID {student.teacher_id} does not exist for student ID {student.name} ({student.name}).")
        except Exception as e:
            print(f"An error occurred while updating student ID {student.name}: {e}")

def update_teacher_performance():
    teachers=Teacher2.objects.all()
    for teacher in teachers:
        try:
            pass_percentage=calculate_teacher_pass_percentage(teacher.emp_id)
            teacher.performance=pass_percentage
            teacher.save()
            print(f"Updated performance for Teacher ID {teacher.emp_id} ({teacher.name}) to {teacher.performance}%")
        except Exception as e:
            print(f"An error occurred while updating performance for Teacher ID {teacher.emp_id}: {e}")

def assign_dept_to_all_schools():
    try:
        # Fetch all active schools
        schools = School.active_objects.all()
        
        # Fetch all active departments
        departments = Departments.active_objects.all()
        
        if not departments.exists():
            print("No active departments to assign.")
            return
        # Iterate through each school and add departments
        for school in schools:
            school.departments.add(*departments)  # Assign all departments to the current school
            print(f"All departments have been assigned to the school: {school.sc_name}")

    except Exception as e:
        print(f"An error occurred: {e}")
    

def make_teacher_as_user():
#Filter Active Teachers
    teachers = Teacher2.objects.filter(is_active=True)
    role=["Teacher","HOD","Principal"]
    #Loop Through Each Active Teacher: 
    for teacher in teachers:
     #Generate Username:
        username = f"{teacher.name.lower().replace(' ', '_')}_{teacher.emp_id}"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits,k=8))
        hashed_password = make_password(random_password)
       
    #Check If Username Already Exists:
        if Users.objects.filter(username=username).exists():
            print(f"Username '{username}' already exists for another user.")
            continue

        name_parts=teacher.name.split(' ',1)
        first_name=name_parts[0]
        last_name=name_parts[1] if len(name_parts)>1 else ''
       
        #If the username does not already exist, a new Users instance is created
        user = Users(
            id=teacher.emp_id,
            username=username,
            password=hashed_password, 
            last_login=timezone.now() ,
            performance=teacher.performance,
            first_name=first_name,
            last_name=last_name,
            sc_id=teacher.sc_id,
            is_active=teacher.is_active,
            created_on=teacher.created_on,
            updated_on=teacher.updated_on,
            role=random.choice(role)
        )
        user.save()
 
        user.department.set(teacher.department.all())
        
        print(f"Created user: {user.username} with a generated password, performance: {user.performance}, "
              f"school ID: {user.sc_id}, departments: {list(user.department.all())}")



def run():
    print("Fetching the data")
    datafetch()
    print("Updating teacher performance...")
    update_teacher_performance()
    print("Assigning departments to the school...")
    assign_dept_to_all_schools()
    print("Making teachers as users...")
    make_teacher_as_user()

if __name__ == "__main__":
    run()
 
