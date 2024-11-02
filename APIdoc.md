# **API Documentation**

This project mainly consists of 4 apps and 31 api endpoints.

1. Student app - 11 api
2. Teacher app - 8 api
3. School app - 6 api
4. Department app - 6 api


# API Endpoints of Student app

## 1. Add New Student

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
1.` HTTP Status: 200 OK`
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

### Messages

1. Student with this roll number already exists.
```python
{
    "rollno": [
        "Student with this roll number already exists."
    ]
}
```
2. Required fields are missing.
```python
{
    "physics": [
        "This field is required."
    ]
}
```



## 2. Retrieve Student Details

* `URL`: http://127.0.0.1:8000/student1/

* `Method` : GET

* `Description`: Retrieves all the student records.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. 
```python
{
        "rollno": 1,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 60.0,
        "chemistry": 60.0,
        "physics": 40.0,
        "total_marks": 160.0,
        "percentage": 53.333333333333336,
        "created_on": "2024-10-25T08:08:28.189842Z",
        "updated_on": "2024-11-02T05:34:17.978209Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    }
```
### Other Responses

1. No Data Available

* HTTP Status: 200 OK

* Description: The request was successful, but no student records are available.

Example Response:
```python
[]
```

2. Internal Server Error

* HTTP Status: 500 Internal Server Error

* Description: An unexpected server error occurred.

* Possible Causes: Database issues, unhandled exceptions, or misconfiguration.

```python
{
  "error": "Internal Server Error",
  "message": "An error occurred while processing the request. Please try again later."
}
```

### Example Messages

1. No Data Available.
```python
[]
```
`Cause`: The request was successful, but there are no student records in the database.

`Solution`: No action needed, but you may want to add student records to the database.

2. Page Not Found
   
* `HTTP Status: 404 Not Found`
```python
{
  "detail": "Not found."
}

```

- **Cause**:
  - **Incorrect URL**: The requested URL doesn’t match any defined route.
  
  - **Resource Missing**: The specific item (e.g., student ID) doesn’t exist in the database.
  - **Routing Issue**: The route might not be properly defined in `urls.py`.

- **Solution**:
  - **Check URL**: Ensure the URL and any IDs are correct.
  - **Validate Resource**: Confirm the resource exists in the database.
  - **Review URL Config**: Verify the endpoint is correctly set up in `urls.py`. 

## 3. Retrieve Student Details by rollno

* `URL`: http://127.0.0.1:8000/student1/byid/<int:rollno>

* `Method` : GET

* `Description`: Retrieves  the student records by rollno.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "rollno": 3,
    "teacher_id": 3,
    "name": "Rahul Kumar",
    "maths": 82.0,
    "chemistry": 77.5,
    "physics": 84.0,
    "total_marks": 243.5,
    "percentage": 81.16666666666667,
    "created_on": "2024-10-25T08:08:28.217296Z",
    "updated_on": "2024-11-02T05:34:34.747297Z",
    "is_active": true,
    "sc_id": 2,
    "dept_id": 1
}
```
### Other Responses

### 1. **Student Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The student with the specified roll number does not exist.
   - **Example Response**:
     ```json
     {
       "detail": "Student with roll number 123 not found."
     }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the roll number format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "Roll number must be a valid integer."
     }
     ```

### 3. **Internal Server Error**

   - **HTTP Status**: `500 Internal Server Error`
   - **Description**: An unexpected server error occurred during the request processing.
   - **Example Response**:
     ```json
     {
       "error": "Internal Server Error",
       "message": "An error occurred while processing the request. Please try again later."
     }
     ```
### Example Messages

### 1. **Successful Retrieval of Student Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "dept_id": 1,
    "sc_id": 1,
    "teacher_id": 1,
    "rollno": 123,
    "chemistry": 85.0,
    "maths": 90.0,
    "physics": 80.0,
    "total_marks": 255.0,
    "percentage": 85.0
  }
  ```

### 2. **Student Not Found**

  ```json
  {
    "detail": "Student with ID 1 not found."
  }
  ```
- **Cause**: The ID provided does not match any existing student record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing student.

### 3. **Bad Request**
- **Response Message**:
  ```json
  {
    "error": "Bad Request",
    "message": "ID must be a valid integer."
  }
  ```
- **Cause**: The ID provided is not in a valid format (e.g., a string instead of an integer).
- **Solution**: Ensure that the ID is provided as a valid integer in the request.

### 4. **Internal Server Error**

- **Response Message**:
  ```json
  {
    "error": "Internal Server Error",
    "message": "An error occurred while processing the request. Please try again later."
  }
  ```
- **Cause**: An unexpected error occurred during the request processing, such as a database issue.
- **Solution**: Check server logs for details about the error and address any underlying issues (e.g., database connectivity).

## 4. Update Student Details

* `URL`: http://127.0.0.1:8000/student1/byid/<int:rollno>

* `Method` : PUT

* `Description`: Update student details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "message": "Student detail updated succesfully"
}
```
### Other Responses

### 1. **Student Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The student with the specified roll number does not exist.
   - **Example Response**:
     ```json
     {
       "detail": "Student with roll number 123 not found."
     }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the roll number format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "Roll number must be a valid integer."
     }
     ```

### 3. **Internal Server Error**

   - **HTTP Status**: `500 Internal Server Error`
   - **Description**: An unexpected server error occurred during the request processing.
   - **Example Response**:
     ```json
     {
       "error": "Internal Server Error",
       "message": "An error occurred while processing the request. Please try again later."
     }
     ```
### Example Messages

### 1. **Successful Retrieval of Student Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "message": "Student detail updated succesfully"
   }
  ```

### 2. **Student Not Found**

  ```json
  {
    "detail": "Student with ID 1 not found."
  }
  ```
- **Cause**: The ID provided does not match any existing student record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing student.

### 3. **Bad Request**
- **Response Message**:
  ```json
  {
    "error": "Bad Request",
    "message": "ID must be a valid integer."
  }
  ```
- **Cause**: The ID provided is not in a valid format (e.g., a string instead of an integer).
- **Solution**: Ensure that the ID is provided as a valid integer in the request.

### 4. **Internal Server Error**

- **Response Message**:
  ```json
  {
    "error": "Internal Server Error",
    "message": "An error occurred while processing the request. Please try again later."
  }
  ```
- **Cause**: An unexpected error occurred during the request processing, such as a database issue.
- **Solution**: Check server logs for details about the error and address any underlying issues (e.g., database connectivity).


## 5. Delete Student Details

* `URL`: http://127.0.0.1:8000/student1/byid/<int:rollno>

* `Method` : DELETE

* `Description`: Delete student details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
DELETE /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    "Student record deleted successfully"
]
```
### Other Responses

### 1. **Student Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The student with the specified roll number does not exist.
   - **Example Response**:
     ```json
     {
       "detail": "Student with roll number 123 not found."
     }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the roll number format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "Roll number must be a valid integer."
     }
     ```

### 3. **Internal Server Error**

   - **HTTP Status**: `500 Internal Server Error`
   - **Description**: An unexpected server error occurred during the request processing.
   - **Example Response**:
     ```json
     {
       "error": "Internal Server Error",
       "message": "An error occurred while processing the request. Please try again later."
     }
     ```
### Example Messages

### 1. **Successful Retrieval of Student Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "message": 
    "Student record deleted successfully"
   }
  ```

### 2. **Student Not Found**

  ```json
  {
    "detail": "Student with ID 1 not found."
  }
  ```
- **Cause**: The ID provided does not match any existing student record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing student.

### 3. **Bad Request**
- **Response Message**:
  ```json
  {
    "error": "Bad Request",
    "message": "ID must be a valid integer."
  }
  ```
- **Cause**: The ID provided is not in a valid format (e.g., a string instead of an integer).
- **Solution**: Ensure that the ID is provided as a valid integer in the request.

### 4. **Internal Server Error**

- **Response Message**:
  ```json
  {
    "error": "Internal Server Error",
    "message": "An error occurred while processing the request. Please try again later."
  }
  ```
- **Cause**: An unexpected error occurred during the request processing, such as a database issue.
- **Solution**: Check server logs for details about the error and address any underlying issues (e.g., database connectivity).

## 6. List of Toppers

* `URL`: http://127.0.0.1:8000/student1/listoftoppers/

* `Method` : GET

* `Description`: returning the top 5 students with the highest total marks .

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 26,
        "teacher_id": 6,
        "name": "Ravi Varma",
        "maths": 92.5,
        "chemistry": 95.0,
        "physics": 94.0,
        "total_marks": 281.5,
        "percentage": 93.83333333333333,
        "created_on": "2024-10-25T08:08:28.458971Z",
        "updated_on": "2024-10-25T08:08:28.458971Z",
        "is_active": false,
        "sc_id": 3,
        "dept_id": 3
    },
    {
        "rollno": 6,
        "teacher_id": 6,
        "name": "Lakshmi Raj",
        "maths": 91.0,
        "chemistry": 90.0,
        "physics": 95.0,
        "total_marks": 276.0,
        "percentage": 92.0,
        "created_on": "2024-10-25T08:08:28.252434Z",
        "updated_on": "2024-10-25T08:08:28.252434Z",
        "is_active": false,
        "sc_id": 3,
        "dept_id": 4
    },
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 7. List of Cutoff

* `URL`: http://127.0.0.1:8000/student1/listofcutoffs/

* `Method` : GET

* `Description`:  Retrieve and return a list of Student data whose total marks are greater than 150.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 1,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 60.0,
        "chemistry": 60.0,
        "physics": 40.0,
        "total_marks": 160.0,
        "percentage": 53.333333333333336,
        "created_on": "2024-10-25T08:08:28.189842Z",
        "updated_on": "2024-11-02T05:34:17.978209Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    },
    {
        "rollno": 2,
        "teacher_id": 2,
        "name": "Sreelakshmi Nair",
        "maths": 75.5,
        "chemistry": 80.0,
        "physics": 88.0,
        "total_marks": 243.5,
        "percentage": 81.16666666666667,
        "created_on": "2024-10-25T08:08:28.208347Z",
        "updated_on": "2024-11-02T05:34:26.010235Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": null
    },
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 8. List of Failed Students

* `URL`: http://127.0.0.1:8000/student1/listoffailed/

* `Method` : GET

* `Description`:  Retrieve and return a failed list of Student.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 27,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 30.0,
        "chemistry": 30.5,
        "physics": 30.0,
        "total_marks": 90.5,
        "percentage": 30.166666666666668,
        "created_on": "2024-10-25T08:23:07.686470Z",
        "updated_on": "2024-10-29T06:33:15.755303Z",
        "is_active": false,
        "sc_id": 1,
        "dept_id": 1
    },
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 9. List of  Students above and below average.

* `URL`: http://127.0.0.1:8000/student1/listofaverage/

* `Method` : GET

* `Description`:  Lists of students who scored above and below the average marks.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "average_marks": 224.11428571428573,
    "students_above_average": [
        {
            "rollno": 2,
            "teacher_id": 2,
            "name": "Sreelakshmi Nair",
            "maths": 75.5,
            "chemistry": 80.0,
            "physics": 88.0,
            "total_marks": 243.5,
            "percentage": 81.16666666666667,
            "created_on": "2024-10-25T08:08:28.208347Z",
            "updated_on": "2024-11-02T05:34:26.010235Z",
            "is_active": true,
            "sc_id": 1,
            "dept_id": null
        },
    ]
    "students_below_average": [
        {
            "rollno": 1,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 60.0,
            "chemistry": 60.0,
            "physics": 40.0,
            "total_marks": 160.0,
            "percentage": 53.333333333333336,
            "created_on": "2024-10-25T08:08:28.189842Z",
            "updated_on": "2024-11-02T05:34:17.978209Z",
            "is_active": true,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
}
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.


## 10. Subjectwise Failed list of students.

* `URL`: http://127.0.0.1:8000/student1/subjectvice/

* `Method` : GET

* `Description`: It retrieves the subjectwise failed list of students.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "failedin_maths": [
        {
            "rollno": 27,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 30.0,
            "chemistry": 30.5,
            "physics": 30.0,
            "total_marks": 90.5,
            "percentage": 30.166666666666668,
            "created_on": "2024-10-25T08:23:07.686470Z",
            "updated_on": "2024-10-29T06:33:15.755303Z",
            "is_active": false,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
    "failedin_chemistry": [
        {
            "rollno": 27,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 30.0,
            "chemistry": 30.5,
            "physics": 30.0,
            "total_marks": 90.5,
            "percentage": 30.166666666666668,
            "created_on": "2024-10-25T08:23:07.686470Z",
            "updated_on": "2024-10-29T06:33:15.755303Z",
            "is_active": false,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
    "failedin_physics": [
        {
            "rollno": 1,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 60.0,
            "chemistry": 60.0,
            "physics": 40.0,
            "total_marks": 160.0,
            "percentage": 53.333333333333336,
            "created_on": "2024-10-25T08:08:28.189842Z",
            "updated_on": "2024-11-02T05:34:17.978209Z",
            "is_active": true,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
}
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 11. Students under the same department.

* `URL`: http://127.0.0.1:8000/student1/bydept/<int:dept_id>/

* `Method` : GET

* `Description`: It retrieves the list of students under the same department.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    [
    {
        "rollno": 1,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 60.0,
        "chemistry": 60.0,
        "physics": 40.0,
        "total_marks": 160.0,
        "percentage": 53.333333333333336,
        "created_on": "2024-10-25T08:08:28.189842Z",
        "updated_on": "2024-11-02T05:34:17.978209Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    },
    {
        "rollno": 3,
        "teacher_id": 4,
        "name": "Rahul Kumar",
        "maths": 82.0,
        "chemistry": 77.5,
        "physics": 84.0,
        "total_marks": 243.5,
        "percentage": 81.16666666666667,
        "created_on": "2024-10-25T08:08:28.217296Z",
        "updated_on": "2024-11-02T18:57:16.210370Z",
        "is_active": true,
        "sc_id": 2,
        "dept_id": 1
    },
    ]
}
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 12. Students under the same school.

* `URL`: http://127.0.0.1:8000/student1/byscid/<int:sc_id>

* `Method` : GET

* `Description`: It retrieves the list of students under the same school.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "failedin_maths": [
        {
            "rollno": 27,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 30.0,
            "chemistry": 30.5,
            "physics": 30.0,
            "total_marks": 90.5,
            "percentage": 30.166666666666668,
            "created_on": "2024-10-25T08:23:07.686470Z",
            "updated_on": "2024-10-29T06:33:15.755303Z",
            "is_active": false,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
    "failedin_chemistry": [
        {
            "rollno": 27,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 30.0,
            "chemistry": 30.5,
            "physics": 30.0,
            "total_marks": 90.5,
            "percentage": 30.166666666666668,
            "created_on": "2024-10-25T08:23:07.686470Z",
            "updated_on": "2024-10-29T06:33:15.755303Z",
            "is_active": false,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
    "failedin_physics": [
        {
            "rollno": 1,
            "teacher_id": 1,
            "name": "Anu",
            "maths": 60.0,
            "chemistry": 60.0,
            "physics": 40.0,
            "total_marks": 160.0,
            "percentage": 53.333333333333336,
            "created_on": "2024-10-25T08:08:28.189842Z",
            "updated_on": "2024-11-02T05:34:17.978209Z",
            "is_active": true,
            "sc_id": 1,
            "dept_id": 1
        },
    ]
}
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 13. Students unde the same teacher.

* `URL`: http://127.0.0.1:8000/student1/stdunderteacher/<int:teacher_id>/

* `Method` : GET

* `Description`: It retrieves the list of students under the same teacher.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 1,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 60.0,
        "chemistry": 60.0,
        "physics": 40.0,
        "total_marks": 160.0,
        "percentage": 53.333333333333336,
        "created_on": "2024-10-25T08:08:28.189842Z",
        "updated_on": "2024-11-02T05:34:17.978209Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    },
    {
        "rollno": 44,
        "teacher_id": 1,
        "name": "Rahul",
        "maths": 85.0,
        "chemistry": 90.0,
        "physics": 30.0,
        "total_marks": 205.0,
        "percentage": 68.33333333333333,
        "created_on": "2024-11-02T18:00:45.936041Z",
        "updated_on": "2024-11-02T18:00:45.936041Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    }
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 14. Students under same department and school.

* `URL`: http://127.0.0.1:8000/student1/studentbydept&sc/<int:dept_id>/<int:sc_id>/

* `Method` : GET

* `Description`: It retrieves the students under the same school and department.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 1,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 60.0,
        "chemistry": 60.0,
        "physics": 40.0,
        "total_marks": 160.0,
        "percentage": 53.333333333333336,
        "created_on": "2024-10-25T08:08:28.189842Z",
        "updated_on": "2024-11-02T05:34:17.978209Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    },
    {
        "rollno": 44,
        "teacher_id": 1,
        "name": "Rahul",
        "maths": 85.0,
        "chemistry": 90.0,
        "physics": 30.0,
        "total_marks": 205.0,
        "percentage": 68.33333333333333,
        "created_on": "2024-11-02T18:00:45.936041Z",
        "updated_on": "2024-11-02T18:00:45.936041Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    }
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 15. Inactivate Student.

* `URL`: http://127.0.0.1:8000/student1/studentdeactivate/<int:rollno>/
  
* `Method` : GET

* `Description`: It inactivates student data.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "message": "Student record set to inactive successfully"
}
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 16. Active Students.

* `URL`: http://127.0.0.1:8000/student1/activestudents/
  
* `Method` : GET

* `Description`: It retrieves the active students.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 1,
        "teacher_id": 1,
        "name": "Anu",
        "maths": 60.0,
        "chemistry": 60.0,
        "physics": 40.0,
        "total_marks": 160.0,
        "percentage": 53.333333333333336,
        "created_on": "2024-10-25T08:08:28.189842Z",
        "updated_on": "2024-11-02T05:34:17.978209Z",
        "is_active": true,
        "sc_id": 1,
        "dept_id": 1
    },
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 17. Inactive Students.

* `URL`:http://127.0.0.1:8000/student1/inactivestudents/

* `Method` : GET

* `Description`: It retrieves inactive students data.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /students HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "rollno": 6,
        "teacher_id": 6,
        "name": "Lakshmi Raj",
        "maths": 91.0,
        "chemistry": 90.0,
        "physics": 95.0,
        "total_marks": 276.0,
        "percentage": 92.0,
        "created_on": "2024-10-25T08:08:28.252434Z",
        "updated_on": "2024-10-25T08:08:28.252434Z",
        "is_active": false,
        "sc_id": 3,
        "dept_id": 4
    },
]
```
### Other Responses

1. **No Students Found (204 No Content)**: 
 
   If there are no students in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No students found."
   }
   ```

2. **Bad Request (400 Bad Request)**:  
   If the request is malformed or contains invalid parameters, return a 400 response with an error message.
   ```json
   {
       "status": "error",
       "message": "Invalid request parameters."
   }
   ```

3. **Internal Server Error (500 Internal Server Error)**:  
   If an unexpected error occurs while processing the request (e.g., database errors), you can return a 500 response.
   ```json
   {
       "status": "error",
       "message": "An internal server error occurred."
   }
   ```
### Messages


### 1. No Students Found (204 No Content)
- **Message**: "No students found."
  - **Cause**: No students in the database or none meet the topper criteria.
  - **Solution**: Verify student data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

