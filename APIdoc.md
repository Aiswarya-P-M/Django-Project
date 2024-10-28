# **API Documentation**

This project mainly consists of 4 apps and 31 api endpoints.

1. Student app - 11 api
2. Teacher app - 8 api
3. School app - 6 api
4. Department app - 6 api


# API Endpoints of Student app

1. Add New Student

* `URL`: http://127.0.0.1:8000/student1/

* `Method` : POST

* `Description`: Adds a new student record with details like name, roll number, and marks.

* `Content-type`:
  
         Content-Type: application/json

* `Body Parameters`:

| Field        | Data Type | Constraints | Relationship                   | Description                                                    |
|--------------|-----------|-------------|--------------------------------|----------------------------------------------------------------|
| `name`       | string    | Required    | -                              | The name of the student.                                       |
| `maths`      | float     | Required    | -                              | The marks obtained in the maths subject.                       |
| `chemistry`  | float     | Required    | -                              | The marks obtained in the chemistry subject.                   |
| `physics`    | float     | Required    | -                              | The marks obtained in the physics subject.                     |
| `teacher_id` | integer   | Optional    | Foreign Key to `Teacher2`     | The ID of the teacher associated with the student, if any.     |
| `sc_id`      | integer   | Optional    | Foreign Key to `School`       | The ID of the school associated with the student, if any.      |
| `dept_id`    | integer   | Optional    | Foreign Key to `Departments`   | The ID of the department associated with the student, if any.  |


* `Fields Automatically Calculated`:

| Field          | Data Type | Constraints       | Description                                                      |
|----------------|-----------|-------------------|------------------------------------------------------------------|
| `rollno`       | integer   | Auto-generated, Primary Key | The unique identifier for the student (do not include in requests). |
| `total_marks`  | float     | Calculated        | The sum of marks obtained in maths, chemistry, and physics.      |
| `percentage`    | float     | Calculated        | Calculated as (total_marks / 300) * 100.                        |
| `created_on`   | datetime  | Auto-generated    | Timestamp when the record is created.                            |
| `updated_on`   | datetime  | Auto-updated      | Timestamp when the record is last modified.                     |





### Example Request

```http
POST /students HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "name": "Shifana",
  "maths": 85.5,
  "chemistry": 90.0,
  "physics": 88.0,
  "teacher_id": 2,
  "sc_id": 1,
  "dept_id": 3
}
```
### Example Reponse
1. 
```
[
    "message:Student Details Added Successfully"
]
```


### Other Responses
1. `400 Bad Request`

**Description:** The request was malformed or some required data is missing or incorrect.

**Possible Causes:**

* Required fields like name, maths, chemistry, or physics are missing.
  
* Data types are incorrect (e.g., a string instead of a float for marks).

* Invalid values (e.g., negative numbers for marks)

### Example
```python
{
  "error": "Bad Request",
  "message": "Field 'maths' is required and must be a positive float."
}
```
2. `409 Conflict`
   
**Description**: The request conflicts with an existing resource or violates a unique constraint.

**Possible Causes**:

A unique constraint on fields (if, for example, student names must be unique).

### Example
```python
{
  "error": "Conflict",
  "message": "A student with this roll number already exists."
}
```
3. `500 Internal Server Error`
   
**Description**: An unexpected error occurred on the server.

**Possible Causes**:

* Database issues, such as a connection error.

* Unhandled server exception.
  
### Example
```python
{
  "error": "Internal Server Error",
  "message": "An error occurred while processing the request. Please try again later."
}
```

1. Retrieve All Students

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