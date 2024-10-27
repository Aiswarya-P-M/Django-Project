# **API Documentation of Student Project**

## Structure of the Project

The project is named a myproject. In django we can create a project using the command
```python
django-admin startproject myproject
```
After the creation of project we need to navigate to  the project directory. For that run the command in terminal
```python
cd myproject
``` 
Then we need to create a virtual environment.Virtual environments in Python allow you to create isolated spaces for your projects, each with its own set of dependencies and package versions. This is especially useful when working on multiple projects with differing requirements or to prevent dependency conflicts. For creating the virtual environment run the command
```python
python -m venv myenv
```
After creating the virtual environment activate it.
```python
myenv\Scripts\activate
``` 
This project mainly consists of 4 apps

1. App2 (For Student)
2. Teacher App
3. School App
4. Department App

## **App2**

### => For creating the  app run the command 
```
python manage.py startapp App2
python manage.py startapp app_Teacher
python manage.py startapp app_School
python manage.py startapp app_Department

```
### => Configure the settings.py file by adding the installed apps inside the installed apps.
```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Myapp",
    "rest_framework",
    "App2",
    "django_extensions",
    "app_School",
    "app_Department",
    "app_Teacher",
```
### => Create models.py file for Student App
```
class Student1(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.AutoField(primary_key=True)
    maths=models.FloatField()
    chemistry=models.FloatField()
    physics=models.FloatField()
    total_marks=models.FloatField(editable=False)
    percentage=models.FloatField(editable=False)
    teacher_id = models.ForeignKey('app_Teacher.Teacher2', on_delete=models.DO_NOTHING,null=True,blank=True)
    sc_id = models.ForeignKey(School, on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_id=models.ForeignKey(Departments, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs): 
        self.total_marks = self.maths + self.chemistry + self.physics
        self.percentage = (self.total_marks / 300) * 100
        super(Student1, self).save(*args, **kwargs) 
```

This `Student1` model represents a student's academic information and includes fields for personal details, academic scores, relationships with other models, and automatically calculated fields.

### Explanation of Each Field

- **name**: Stores the student's name as a character field, with a maximum length of 50 characters.
- **rollno**: An auto-incremented primary key field that uniquely identifies each student.
- **maths**, **chemistry**, **physics**: Float fields for storing the student's scores in these three subjects.
- **total_marks**: A float field to store the sum of scores in all subjects. It is set to `editable=False` because it will be calculated automatically and should not be manually modified.
- **percentage**: A float field for storing the calculated percentage. It is also set to `editable=False` to prevent manual editing.
- **teacher_id**: A foreign key referencing the `Teacher2` model (from `app_Teacher`), establishing a link between the student and a teacher.
- **sc_id**: A foreign key to a `School` model, representing the school associated with the student.
- **dept_id**: A foreign key to a `Departments` model, linking the student to a specific department.
- **created_on**: Automatically captures the timestamp when a student record is created.
- **updated_on**: Automatically updates the timestamp whenever a student record is modified.

### Custom `save()` Method

The `save()` method is overridden to automatically calculate and set `total_marks` and `percentage` before saving the record:

- `total_marks` is calculated as the sum of `maths`, `chemistry`, and `physics` scores.
- `percentage` is derived by dividing `total_marks` by 300 (assuming each subject is out of 100), then multiplying by 100 to get the percentage.
  
After these calculations, the `super().save()` method saves the record to the database. This approach ensures `total_marks` and `percentage` are always up to date.

### => Register the model in the admin.py file
```
from django.contrib import admin
from .models import *
admin.site.register(Student1)
```
### => Perform Migrations
After creating model migrate it
```
python manage.py makemigrations
python manage.py migrate
```
### => Serializers.py file

The `Student1serializers` class is a Django REST Framework serializer for the `Student1` model. It uses `ModelSerializer` to automatically handle all fields in `Student1` (`fields = "__all__"`), enabling easy conversion between `Student1` instances and JSON format.

- **teacher_id**: Defined with `PrimaryKeyRelatedField`, allowing write access by accepting the primary key of a `Teacher2` instance.
  
### => URL Configuration
Main url configuration is done in the project urls.py file.
from django.contrib import admin
from django.urls import path,include
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path('student1/',include('App2.urls')),
    path('school/',include('app_School.urls')),
    path('dept/',include('app_Department.urls')),
    path('teacher/',include('app_Teacher.urls')),
```
### => Creating functions and API Endpoints
Student API Endpoints

1. Add New Student

* Endpoint: POST /student1/

* Description: Adds a new student record with details like name, roll number, and marks.

2. Retrieve All Students

* Endpoint: GET /student1/

* Description: Fetches a list of all students in the system.

3. Update Student Information

* Endpoint: PUT /student1/<rollno>/

* Description: Updates the information of a specific student using their roll number.

4. Delete Student

* Endpoint: DELETE /student1/<rollno>/

* Description: Removes a student record from the database based on their roll number.

Performance and Analysis API Endpoints

1. Top 5 Students by Marks

* Endpoint: GET /student1/listoftoppers/

* Description: Returns a list of the top 5 students based on total marks.

2. Students Above a Cutoff Score

* Endpoint: GET /student1/listofcutoff/

* Description: Lists students who scored above a cutoff mark (150).

3. Failed Students

* Endpoint: GET /student1/listoffailed/

* Description: Lists students who scored below the passing threshold (35).

4. Average Performance Analysis

* Endpoint: GET /student1/listofaverage/

* Description: Categorizes students into below or above average based on marks.

5. Subject wise failed list
   
* Endpoint: GET /student1/subjectvice/

* Description: Categorizes the subject wise failed students.

### => Views.py Structure
## CRUD operations
1. get(self, request) - Retrieves all student records and returns them in JSON format.

2. delete(self, request) - Deletes all student records from the database.

3. post(self, request) - Creates new student records based on the provided data.
   
## Student1DetailView
1. get(self, request, rollno) - Fetches a specific student's details by their roll number.

2. put(self, request, rollno) - Updates a specific student's details by roll number.

3. delete(self, request, rollno) - Deletes a specific student's record by roll number.
   
## Student1Listtoppers
1. get(self, request) - Retrieves the top 5 students based on their total marks.
   
## Student1LitofcutoffsView
1. get(self, request) - Lists students who scored above a total of 150 marks.
   
## Student1ListofFailedView
1. get(self, request) - Lists students with a total score of 150 or below, indicating a failure status.

## Student1ListofaverageView
1. get(self, request) - Calculates the average mark and categorizes students into above or below average.

## StudentsubjectwisefailedlistView
1. get(self, request) - Lists students who failed in each subject, using a cutoff mark of 50.

## =>URL Pattern
```python
from django.urls import path
from .views import *

urlpatterns=[
    path('',Student1View.as_view(),name='list_student'),
    path('byid/<int:rollno>',Student1DetailView.as_view(),name='studentdetails_byid'),
    path('listoftoppers/',Student1Listtoppers.as_view(),name='studentlistoftoppers'),
    path('listofcutoffs/',Student1LitofcutoffsView.as_view(),name='studentlistofcutoffs'),
    path('listoffailed/',Student1ListofFailedView.as_view(),name='studentlistoffailed'),
    path('listofaverage/',Student1ListofaverageView.as_view(),name='studentlistofaverage'),
    path('subjectvice/',StudentsubjectwisefailedlistView.as_view(),name='subjectvicefailedlist'),
```
## =>utils.py

The utils.py file contains utility functions that support calculations and data processing for student performance and teacher metrics in the application. These functions simplify complex operations and are reusable across different parts of the codebase.

```python
from .models import *

def calculate_average_marks(total_students: int, total_marks_sum: float):
    return (total_marks_sum / total_students) if total_students > 0 else 0


def get_subjectwise_failed(cutoff_marks):
    failedin_maths=Student1.objects.filter(maths__lt=cutoff_marks)
    failedin_chemistry=Student1.objects.filter(chemistry__lt=cutoff_marks)
    failedin_physics=Student1.objects.filter(physics__lt=cutoff_marks)
    return {
            'failedin_maths':failedin_maths,
            'failedin_chemistry':failedin_chemistry,
            'failedin_physics':failedin_physics,
    } 
def calculate_teacher_pass_percentage(teacher_id):
    # Count the total number of students for the given teacher
    total_students = Student1.objects.filter(teacher_id=teacher_id).count()
    
    # Count passed students for the teacher (total_marks > 150)
    passed_students_count = Student1.objects.filter(teacher_id=teacher_id, total_marks__gt=150).count()

    if total_students > 0:
        # Calculate pass percentage
        pass_percentage = (passed_students_count / total_students) * 100
        return round(pass_percentage,2)
    
    return 0
```
Function Descriptions

```calculate_average_marks(total_students: int, total_marks_sum: float)```

**Calculates the average marks for a group of students**.

Parameters:

```total_students```: The total number of students.

`total_marks_sum`: The sum of marks for all students.

`Returns`: Average marks or 0 if there are no students.

**get_subjectwise_failed(cutoff_marks)**

Retrieves students who scored below a specific cutoff mark in each subject.

Parameters:

`cutoff_marks`: The threshold score below which a student is considered to have failed.

`Returns`: A dictionary with lists of students who failed in maths, chemistry, and physics.

`calculate_teacher_pass_percentage(teacher_id)`

**Calculates the pass percentage for a teacher’s students, based on the number of students who scored above 150.**

Parameters:

`teacher_id`: The ID of the teacher whose student pass rate is calculated.

`Returns`: The pass percentage (rounded to two decimal places) or 0 if the teacher has no students.

## **Teacher App**

### => Models.py file
```python
from django.db import models
from app_School.models import School  # Import School from the app_School app
from app_Department.models import Departments  # Import Department from the app_Department app

# Create your models here.
class Teacher2(models.Model):
    name=models.CharField(max_length=50)
    emp_id=models.AutoField(primary_key=True)
    performance=models.FloatField(default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_id=models.ForeignKey('app_Department.Departments', on_delete=models.DO_NOTHING, null=True, blank=True)
```
The `Teacher2` model represents teachers and includes fields for personal details, performance metrics, and associations with school and department.

### Field Descriptions

- **name**: Stores the teacher's name as a character field, with a maximum length of 50.
- **emp_id**: An auto-incremented primary key field that uniquely identifies each teacher.
- **performance**: A float field representing the teacher's performance score, with a default value of 0.
- **created_on**: Automatically captures the timestamp when a teacher record is created.
- **updated_on**: Automatically updates the timestamp whenever a teacher record is modified.
- **sc_id**: A foreign key linking to a `School` model from `app_School`, indicating the school associated with the teacher.
- **dept_id**: A foreign key linking to a `Departments` model from `app_Department`, representing the department associated with the teacher. 

This model allows for capturing essential information about each teacher, their affiliation, and performance metrics.

### => Admin Registration
```python
admin.site.register(Teacher2)
```
### => Serializers
```python
class Teacherserializers(serializers.ModelSerializer):
    sc_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    dept_id = serializers.PrimaryKeyRelatedField(queryset=Departments.objects.all())
    class Meta:
        model=Teacher
        fields="__all__"
```
The `Teacherserializers` class is a Django REST Framework serializer for the `Teacher` model, handling all fields (`fields="__all__"`). It includes:

- **sc_id** and **dept_id**: Allow write access by accepting primary keys for related `School` and `Departments` instances.

This serializer enables full CRUD operations for teacher records via the API.
### => API Endpoints

Here are the API endpoints for the Teacher app, organized by CRUD operations followed by additional functions:

### Teacher API Endpoints

#### CRUD Operations

1. **Add New Teacher**
   - **Endpoint**: `POST /teacher/`
   - **Description**: Adds a new teacher record with details such as name and department.

2. **Retrieve All Teachers**
   - **Endpoint**: `GET /teacher/`
   - **Description**: Returns a list of all teachers in the system.

3. **Get Teacher Details**
   - **Endpoint**: `GET /teacher/<teacher_id>/`
   - **Description**: Fetches details of a specific teacher by their employee ID.

4. **Delete All Teachers**
   - **Endpoint**: `DELETE /teacher/`
   - **Description**: Deletes all teacher records from the database.

5. **Update Student Performance on Addition**
   - **Endpoint**: `POST /teacher/updateperbyadd/`
   - **Description**: Adds a new student and updates the associated teacher's performance percentage.

6. **Delete Student and Update Teacher Performance**
   - **Endpoint**: `DELETE /teacher/performanceupdate/<int:rollno>/`
   - **Description**: Deletes a specific student record by roll number and updates the associated teacher's performance percentage.

7. **Update Student Information and Teacher Performance**
   - **Endpoint**: `PUT /teacher/performanceupdate/<int:rollno>/`
   - **Description**: Updates a specific student's details and adjusts the associated teacher's performance percentage accordingly.

#### Performance and Analysis Functions

1. **Get Teacher Performance Overview**
   - **Endpoint**: `GET /teacher/performance/`
   - **Description**: Retrieves a list of teachers categorized as best performers (≥ 75% pass rate) and those needing improvement.

## => Structure of views.py
Here's a more concise explanation of the `views.py` file:

### `views.py` Overview

1. **TeacherPerformanceView** (`get(self, request)`)
   - Retrieves and categorizes teachers based on pass percentage, identifying top performers.

2. **teacherdetailsView** (`get(self, request, teacher_id)`)
   - Fetches details of a specific teacher by `teacher_id`. Returns a 404 error if not found.

3. **TeacherallDetailsView**
   - **`get(self, request)`**: Lists all teachers.
   - **`post(self, request)`**: Adds new teacher records if valid; returns errors if invalid.
   - **`delete(self, request)`**: Deletes all teacher records.

4. **updateperbyaddView** (`post(self, request)`)
   - Adds a new student and updates the associated teacher's performance. Returns an error if no teacher is linked.

5. **performanceupdateView**
   - **`delete(self, request, rollno)`**: Deletes a student by `rollno` and updates the teacher's performance; returns errors if not found.
   - **`put(self, request, rollno)`**: Updates a student's details and recalculates the teacher's performance; returns errors if validation fails.

## =>URL Pattern
```python
from django.urls import path
from .views import *

urlpatterns=[
    path('teachperformance/',TeacherPerformanceView.as_view(),name='teachersperformance'),
    path('byid/<int:teacher_id>/',teacherdetailsView.as_view(),name='teacherdetails'),
    path('crud/',TeacherallDetailsView.as_view(),name='teachersalldetails'),
    path('updateperbyadd/',updateperbyaddView.as_view(),name='updateper'),
    path('performanceupdate/<int:rollno>/',performanceupdateView.as_view(),name='performanceupdate'),
    

]
```
### => Overview of Scripts.py file


This script performs two main tasks: updating student-teacher associations and recalculating teacher performance metrics.

```python
from App2.models import Student1
from app_Teacher.models import Teacher2 
from App2.utils import calculate_teacher_pass_percentage



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

def run():
    print("Fetching the data")
    datafetch()
    print("Updating teacher performance...")
    update_teacher_performance()
 
if __name__ == "__main__":
    run()
 
```

1. **Function: `datafetch()`**
   - **Purpose**: Associates each student with their corresponding teacher.
   - **Process**:
     - Retrieves teacher IDs from the `Teacher2` model.
     - Iterates through all students, checking if their `teacher_id` exists among the fetched IDs.
     - Updates students with the appropriate teacher object and saves the changes, printing confirmation or error messages.

2. **Function: `update_teacher_performance()`**
   - **Purpose**: Updates the performance percentage for each teacher.
   - **Process**:
     - Iterates through all teachers and calculates their pass percentage using the utility function `calculate_teacher_pass_percentage()`.
     - Updates the teacher's performance attribute and saves it, printing confirmation or error messages.

3. **Function: `run()`**
   - **Purpose**: Executes the main tasks of the script.
   - **Process**:
     - Calls `datafetch()` to update student-teacher links.
     - Calls `update_teacher_performance()` to refresh teachers' performance metrics.

4. **Execution Block**:
   - The script runs the `run()` function when executed as the main module.
  

## **School App**

### => Models.py file
```python
from django.db import models
# from app_Department import models as department_models
# Create your models here.

class School(models.Model):
    sc_name=models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sc_id=models.AutoField(primary_key=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

```
This models.py file defines the School model for a Django application, representing educational institutions in the database.

School Model

Attributes:

`sc_name`: A character field (string) for the school's name, with a maximum length of 100 characters.

`location`: A character field for the school's location, also with a maximum length of 100 characters.

`sc_id`: An auto-incrementing primary key field that uniquely identifies each school.

`created_on`: A timestamp that records when the school record was created, automatically set upon creation.

`updated_on`: A timestamp that updates automatically whenever the school record is modified.

### => Admin Registration
```python
admin.site.register(School)
```
### => Serializers
```python
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
```


This file defines the `SchoolSerializer`, which is used for converting `School` model instances to and from JSON for API communication.

#### `SchoolSerializer` Class

- **Inherits from**: `serializers.ModelSerializer`.
- **Meta Class**:
  - **model**: Links to the `School` model.
  - **fields**: Set to `'__all__'`, including all model fields in serialization.

### => API Endpoints

Here are the API endpoints for the School app, organized by CRUD operations followed by additional functions:

### School API Endpoints

#### CRUD Operations

1. **Add New School**
   - **Endpoint**: `POST /school/`
   - **Description**: Adds a new school record with details such as school name,location and id.

2. **Retrieve All School**
   - **Endpoint**: `GET /school/`
   - **Description**: Returns a list of all school in the database.

3. **Get School Details**
   - **Endpoint**: `GET /school/<sc_id>/`
   - **Description**: Fetches details of a specific school by the school ID.

4. **Delete All School data**
   - **Endpoint**: `DELETE /school/`
   - **Description**: Deletes all school records from the database.

5. **Update School by school id**
   - **Endpoint**: `PUT /school/byid/<int:sc_id>`
   - **Description**: Update school details.

6. **Delete School by id**: `DELETE /school/byid/<int:sc_id>/`
   - **Description**: Deletes a specific school record by school id.

## => Structure of views.py
Here's a more concise explanation of the `views.py` file:

### `SchoolcreateView` Class
Handles creating and retrieving school records.

- **`get(self, request)`**: 
  - Retrieves all school records and returns them as a JSON response with a 200 OK status.

- **`post(self, request)`**: 
  - Validates and saves new school data. Responds with a success message (201 Created) or validation errors (400 Bad Request).

- **`delete(self, request)`**: 
  - Deletes all school records. Returns a success message or a 400 Bad Request on error.

### `SchooldetailsView` Class
Manages individual school records by ID.

- **`get(self, request, sc_id)`**: 
  - Fetches a school record by its ID and returns it as a JSON response. Returns a 404 Not Found error if not found.

- **`put(self, request, sc_id)`**: 
  - Updates the specified school record with new data. Returns a success message or validation errors.

- **`delete(self, request, sc_id)`**: 
  - Deletes the specified school record and returns a success message or a 404 Not Found error if the record does not exist.

### Summary
These views provide CRUD operations for school records, managing both collections and individual records effectively.

## =>URL Pattern
```python
from django.urls import path
from .views import *

urlpatterns=[
    path('',SchoolcreateView.as_view(),name='create_school'),
    path('byid/<int:sc_id>',SchooldetailsView.as_view(),name='school_details')
]
```
## **Department App**

### => Models.py file
```python
from django.db import models
# from app_School import models as school_model
# from App2 import models as Teacher_model
# Create your models here.
# from App2.models import Teacher

class Departments(models.Model):
    hod_name=models.ForeignKey('app_Teacher.Teacher2',on_delete=models.DO_NOTHING,null=True,blank=True)
    dept_name=models.CharField(max_length=100)
    dept_id=models.AutoField(primary_key=True)
    sc_id = models.ForeignKey('app_School.School', on_delete=models.DO_NOTHING,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    
```
The `models.py` file defines a `Departments` model with the following fields:

- **`hod_name`**: A foreign key linking to the `Teacher2` model, representing the head of the department. It can be null or blank.
- **`dept_name`**: A character field for the name of the department, limited to 100 characters.
- **`dept_id`**: An auto-incrementing primary key for the department.
- **`sc_id`**: A foreign key linking to the `School` model, representing the school to which the department belongs. It can also be null or blank.
- **`created_on`**: A timestamp indicating when the department record was created, automatically set.
- **`updated_on`**: A timestamp indicating when the department record was last updated, automatically set.

This model facilitates the organization of departments within schools and associates them with their respective heads and schools.

### => Admin Registration
```python
admin.site.register(Department)
```
### => Serializers
```python
from rest_framework import serializers
from .models import Departments
from app_School.models import School

class DeptSerializer(serializers.ModelSerializer):
    sc_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    class Meta:
        model = Departments
        fields = '__all__'
```
The `serializers.py` file defines a `DeptSerializer` class, which is a serializer for the `Departments` model. Here's a brief explanation:

- **`DeptSerializer`**: This class inherits from `serializers.ModelSerializer`, allowing it to automatically handle the serialization and deserialization of `Departments` instances.
- **`sc_id`**: This field is a `PrimaryKeyRelatedField`, which establishes a relationship with the `School` model. It ensures that only valid school IDs from the `School` queryset can be assigned.
- **`Meta` class**: Specifies the model to be serialized (`Departments`) and includes all fields from the model (`fields = '__all__'`).

Overall, this serializer facilitates the conversion of `Departments` model instances to and from JSON format, ensuring that relationships with the `School` model are properly handled.

### => API Endpoints

Here are the API endpoints for the Department app, organized by CRUD operations followed by additional functions:

### Department API Endpoints

#### CRUD Operations

1. **Add New Department**
   - **Endpoint**: `POST /dept/`
   - **Description**: Adds a new department record with details such as department name,hod name department id and school id.

2. **Retrieve All Departments**
   - **Endpoint**: `GET /dept/`
   - **Description**: Returns a list of all departments in the database.

3. **Get Department Details**
   - **Endpoint**: `GET /dept/byid/<int:dept_id>`
   - **Description**: Fetches details of a specific department by the department ID.

4. **Delete All Department data**
   - **Endpoint**: `DELETE /dept/`
   - **Description**: Deletes all department records from the database.

5. **Update Department by Department id**
   - **Endpoint**: `PUT /dept/byid/<int:dept_id>`
   - **Description**: Update Department details.

6. **Delete Department by id**: `DELETE /dept/byid/<int:dept_id>`
   - **Description**: Deletes a specific department record by department id.

## => Structure of views.py
Here's a more concise explanation of the `views.py` file:

### `DeptcreateView(APIView)`

1. **`get(self, request)`**:
   - Fetches all departments.
   - Returns a JSON list of departments with a 200 OK status.

2. **`post(self, request)`**:
   - Adds new departments based on request data.
   - Returns a success message with a 201 Created status if valid; otherwise, validation errors with a 400 Bad Request status.

3. **`delete(self, request)`**:
   - Deletes all departments.
   - Returns a success message with a 200 OK status; returns a 400 Bad Request on error.

### `DeptdetailsView(APIView)`

4. **`get(self, request, dept_id)`**:
   - Retrieves a specific department by its ID.
   - Returns department details with a 200 OK status or an error message with a 404 Not Found status if not found.

5. **`put(self, request, dept_id)`**:
   - Updates a department's details.
   - Returns a success message with a 200 OK status if successful; otherwise, validation errors with a 400 Bad Request status.

6. **`delete(self, request, dept_id)`**:
   - Deletes a specific department by its ID.
   - Returns a success message with a 200 OK status if found and deleted; returns a 404 Not Found status if not found.

This file implements CRUD operations for department records in a Django REST framework application.

## =>URL Pattern
```python
from django.urls import path
from .views import *

urlpatterns=[
    path('',DeptcreateView.as_view(),name='create_department'),
    path('byid/<int:dept_id>',DeptdetailsView.as_view(),name='department_details')
]
```