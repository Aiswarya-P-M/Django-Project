# **API Documentation**

This project mainly consists of 4 apps and 31 api endpoints.

1. Student app - 17 api
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

# API Endpoints of Teacher app

## 1. Create Teacher

* `URL`: http://127.0.0.1:8000/teacher/

* `Method` : POST

* `Description`: Adds a new teacher record with details like name, school id, and department.

* `Content-type`:
  
         Content-Type: application/json

* `Body Parameters`:

# Teacher2 Model

| Field         | Data Type   | Constraints             | Relationship                      | Description                                                       |
|---------------|-------------|-------------------------|-----------------------------------|-------------------------------------------------------------------|
| `name`        | string      | Required               | -                                 | The name of the teacher.                                          |
| `emp_id`      | integer     | Primary Key, AutoField | -                                 | A unique identifier for each teacher.                             |
| `performance` | float       | Default = 0            | -                                 | The performance score of the teacher.                             |
| `created_on`  | DateTime    | Auto-generated         | -                                 | The date and time when the record was created.                    |
| `updated_on`  | DateTime    | Auto-updated           | -                                 | The date and time when the record was last updated.               |
| `sc_id`       | Foreign Key | Optional               | Foreign Key to `School`           | The ID of the school associated with the teacher.                 |
| `is_active`   | boolean     | Default = True         | -                                 | Indicates if the teacher record is active.                        |
| `department`  | ManyToMany  | -                      | ManyToManyField to `Departments`  | The departments associated with the teacher.                      |





### Example Request

```http
POST /teacher HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "name": "Sandra",
    "sc_id": 4,
    "department": [1]  
}


```
### Example Reponse
1.` HTTP Status: 200 OK`
```
{
    "emp_id": 34,
    "sc_id": 4,
    "department": [
        1
    ],
    "name": "Sandra",
    "performance": 0.0,
    "created_on": "2024-11-03T17:29:39.500432Z",
    "updated_on": "2024-11-03T17:29:39.500432Z",
    "is_active": true
}
```

### Other Responses

---

### Possible Responses for Creating a New Teacher

1. **`201 Created`**

   **Description:** The teacher was successfully created.

   **Example:**
   ```json
   {
    "emp_id": 35,
    "sc_id": 4,
    "department": [
        2
    ],
    "name": "Pooja",
    "performance": 0.0,
    "created_on": "2024-11-03T17:43:19.025136Z",
    "updated_on": "2024-11-03T17:43:19.025136Z",
    "is_active": true
    }
   ```

---

2. **`400 Bad Request - Missing or Invalid Fields`**

   **Description:** Some required fields are missing, have incorrect data types, or contain invalid values.

   **Possible Causes:**

   * Required fields like `name` or `sc_id` are missing.
   * Invalid data types (e.g., providing a string instead of a float for `performance`).
   * Values out of valid range (e.g., negative values for `performance`).

   **Example:**
   ```json
   {
       "error": "Bad Request",
       "message": "Field 'name' is required.",
       "fields": {
           "performance": ["Performance must be a non-negative float."]
       }
   }
   ```

---

3. **`400 Bad Request - Department Not in School`**

   **Description:** The selected department is not associated with the specified school.

   **Possible Causes:**

   * The `dept_id` does not match any department listed under the specified `sc_id`.

   **Example:**
   ```json
   {
       "non_field_errors": [
           "The department 'Zoology' is not under the selected school 'Bharathiya Vidya Bhavan'."
       ]
   }
   ```

---


4. **`404 Not Found - School or Department Does Not Exist`**

   **Description:** The specified school or department was not found.

   **Possible Causes:**

   * The `sc_id` or `dept_id` provided does not exist in the database.

   **Example:**
   ```json
   {
       "error": "Not Found",
       "message": "The specified school or department was not found."
   }
   ```

---

5. **`405 Method Not Allowed`**

   **Description:** The HTTP method used is not supported for this endpoint.

   **Possible Causes:**

   * Using an unsupported method like GET instead of POST.

   **Example:**
   ```json
   {
       "error": "Method Not Allowed",
       "message": "The requested method is not allowed for this resource."
   }
   ```

---

6. **`500 Internal Server Error`**

    **Description:** An unexpected server error occurred.

    **Possible Causes:**

    * Database issues, such as connection errors.
    * Unhandled server exceptions during the processing of the request.

    **Example:**
    ```json
    {
        "error": "Internal Server Error",
        "message": "An error occurred while processing the request. Please try again later."
    }
    ```

---

### Messages

Here’s a more concise version of the error responses for creating a teacher.

---

---

1. **Missing Required Fields**

   ```json
   {
       "name": [
           "This field is required."
       ],
       "sc_id": [
           "This field is required."
       ]
   }
   ```

---

2. **Department Not in School**

   ```json
   {
       "non_field_errors": [
           "The department 'Zoology' is not under the selected school."
       ]
   }
   ```

---


---

3. **Invalid Data Type**

   ```json
   {
       "sc_id": [
           "A valid integer is required."
       ]
   }
   ```

---

---

4. **Invalid Department Selection**

   ```json
   {
       "department": [
           "Select a valid choice."
       ]
   }
   ```

---

5. **Inactive School**

   ```json
   {
       "sc_id": [
           "The selected school is inactive."
       ]
   }
   ```



## 2. Retrieve Teacher Details

* `URL`: http://127.0.0.1:8000/teacher/

* `Method` : GET

* `Description`: Retrieves all the teacher records.

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
[
    {
        "emp_id": 1,
        "sc_id": 1,
        "department": [
            1
        ],
        "name": "Anjali Menon",
        "performance": 50.0,
        "created_on": "2024-10-25T07:32:18.465411Z",
        "updated_on": "2024-11-02T17:25:22.506775Z",
        "is_active": true
    },
    {
        "emp_id": 2,
        "sc_id": 2,
        "department": [
            1,
            2
        ],
        "name": "Suresh Nair",
        "performance": 75.0,
        "created_on": "2024-10-25T07:32:18.480441Z",
        "updated_on": "2024-11-02T06:27:37.582156Z",
        "is_active": true
    },
]
```
### Other Responses

1. No Data Available

* HTTP Status: 200 OK

* Description: The request was successful, but no teacher records are available.

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
`Cause`: The request was successful, but there are no teacher records in the database.

`Solution`: No action needed, but you may want to add teacher records to the database.

2. Page Not Found
   
* `HTTP Status: 404 Not Found`
```python
{
  "detail": "Not found."
}

```

- **Cause**:
  - **Incorrect URL**: The requested URL doesn’t match any defined route.
  
  - **Resource Missing**: The specific item (e.g., teacher ID) doesn’t exist in the database.
  - **Routing Issue**: The route might not be properly defined in `urls.py`.

- **Solution**:
  - **Check URL**: Ensure the URL and any IDs are correct.
  - **Validate Resource**: Confirm the resource exists in the database.
  - **Review URL Config**: Verify the endpoint is correctly set up in `urls.py`. 

## 3. Retrieve teacher Details by id

* `URL`: http://127.0.0.1:8000/teacher/byid/<int:emp_id>

* `Method` : GET

* `Description`: Retrieves  the teacher records by id.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /teacher HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "teacher": {
        "emp_id": 2,
        "sc_id": 2,
        "department": [
            1,
            2
        ],
        "name": "Suresh Nair",
        "performance": 75.0,
        "created_on": "2024-10-25T07:32:18.480441Z",
        "updated_on": "2024-11-02T06:27:37.582156Z",
        "is_active": true
    }
}
```
### Other Responses

### 1. **Teacher Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The teacher with the specified id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "Teacher not found."
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "emp_id must be a valid integer."
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
    "teacher": {
        "emp_id": 2,
        "sc_id": 2,
        "department": [
            1,
            2
        ],
        "name": "Suresh Nair",
        "performance": 75.0,
        "created_on": "2024-10-25T07:32:18.480441Z",
        "updated_on": "2024-11-02T06:27:37.582156Z",
        "is_active": true
    }
  }
  ```

### 2. **teacher Not Found**

  ```json
  {
    "error": "Teacher not found."
}
  ```
- **Cause**: The ID provided does not match any existing teacher record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing teacher.

### 3. **Bad Request**
- **Response Message**:
  ```json
  {
    "error": "Bad Request",
    "message": "emp_id must be a valid integer."
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

## 4. Update teacher Details

* `URL`: http://127.0.0.1:8000/student1/byid/<int:emp_id>

* `Method` : PUT

* `Description`: Update teacher details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /teacher HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "emp_id": 2,
    "sc_id": 1,
    "department": [
        1,
        2
    ],
    "name": "Anjali Menon",
    "performance": 75.0,
    "created_on": "2024-10-25T07:32:18.480441Z",
    "updated_on": "2024-11-03T18:01:09.421828Z",
    "is_active": true
}
```
### Other Responses

### 1. **Teacher Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The teacher with the specified emp_id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "Teacher not found"
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the emp_id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "emp_id must be a valid integer."
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

### 1. **Successful Retrieval of teacher Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "emp_id": 1,
    "sc_id": 1,
    "department": [
        1,
        2
    ],
    "name": "Anjali Menon",
    "performance": 50.0,
    "created_on": "2024-10-25T07:32:18.465411Z",
    "updated_on": "2024-11-03T18:07:33.785160Z",
    "is_active": true
  }
  ```

### 2. **Teacher Not Found**

  ```json
  {
    "error": "Teacher not found"
}
  ```
- **Cause**: The ID provided does not match any existing teacher record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing teacher.

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


## 5. Delete Teacher Details

* `URL`: http://127.0.0.1:8000/teacher/byid/<int:emp_id>

* `Method` : DELETE

* `Description`: Delete teacher details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
DELETE /teacher HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "message": "Teacher data deleted successfully"
}
```
### Other Responses

### 1. **Teacher Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The teacher with the specified emp_id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "Teacher not found"
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the emp_id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "emp_id must be a valid integer."
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

### 1. **Successful Retrieval of teacher Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "message": 
    "Teacher data deleted successfully"
   }
  ```

### 2. **Teacher Not Found**

  ```json
  {
    "error": "Teacher not found"
}
  ```
- **Cause**: The ID provided does not match any existing teacher record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing teacher.

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

## 6. Performance of teachers

* `URL`: http://127.0.0.1:8000/teacher/teachperformance/

* `Method` : GET

* `Description`: returning the performance of teachers.

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
    "best_teachers": [
        {
            "teacher_name": "Anjali Menon",
            "pass_percentage": 100.0
        },
        {
            "teacher_name": "Anjali Menon",
            "pass_percentage": 100.0
        },
        {
            "teacher_name": "Ravi Kumar",
            "pass_percentage": 100.0
        },
        {
            "teacher_name": "Lakshmi Iyer",
            "pass_percentage": 100.0
        }
    ],
    "teachers_needing_improvement": [
        {
            "teacher_name": "Deepa Pillai",
            "pass_percentage": 0
        },
        {
            "teacher_name": "Vinod Das",
            "pass_percentage": 0
        },
    ]
}
```
### Other Responses

1. **No teacher Found (204 No Content)**: 
 
   If there are no teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No teachers found."
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


### 1. No Teachers Found(204 No Content)
- **Message**: "No Teachers found."
  - **Cause**: No teachers in the database or none meet the topper criteria.
  - **Solution**: Verify teacher data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 7. Update performance of teacher by adding the student data

* `URL`: http://127.0.0.1:8000/teacher/updateperbyadd/

* `Method` : POST

* `Description`:  Update the performance of teacher by adding a new student.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
POST /teachers HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "message": "Student details added successfully, and teacher performance updated."
}
```
### Other Responses

1. **No Teacher Found (204 No Content)**: 
 
   If there are no teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No teachers found."
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


### 1. No Teachers Found (204 No Content)
- **Message**: "No teachers found."
  - **Cause**: No teachers in the database or none meet the topper criteria.
  - **Solution**: Verify steachers data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 8. Updating the performance of teacher by updating the data

* `URL`: http://127.0.0.1:8000/teacher/updateperbydel/<int:rollno>/

* `Method` : PUT

* `Description`:  Updating the performance of teacher by updating the student data.

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
    "rollno": 1,
    "teacher_id": 1,
    "name": "Anu",
    "maths": 60.0,
    "chemistry": 60.0,
    "physics": 40.0,
    "total_marks": 160.0,
    "percentage": 53.333333333333336,
    "created_on": "2024-10-25T08:08:28.189842Z",
    "updated_on": "2024-11-03T18:27:22.077409Z",
    "is_active": true,
    "sc_id": 1,
    "dept_id": 1
}
```
### Other Responses

1. **No Student Found (204 No Content)**: 
 
   If there are no st in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
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

## 9. Updating the performance of teacher by deleting the student data.

* `URL`: http://127.0.0.1:8000/teacher/updateperbydel/<int:rollno>/

* `Method` : DELETE

* `Description`:  Updating the performance of teacher by deleting the student data.

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
{
    "message": "Student Divya Chandran deleted successfully."
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


## 10. Teachers under the same school.

* `URL`: http://127.0.0.1:8000/teacher/byschool/<int:sc_id>/

* `Method` : GET

* `Description`: It retrieves the list of teachers under the same school.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /teachers HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "emp_id": 1,
        "sc_id": 1,
        "department": [
            1,
            2
        ],
        "name": "Anjali Menon",
        "performance": 100.0,
        "created_on": "2024-10-25T07:32:18.465411Z",
        "updated_on": "2024-11-03T18:32:10.674992Z",
        "is_active": true
    },
    {
        "emp_id": 2,
        "sc_id": 1,
        "department": [
            1,
            2
        ],
        "name": "Anjali Menon",
        "performance": 100.0,
        "created_on": "2024-10-25T07:32:18.480441Z",
        "updated_on": "2024-11-03T18:32:10.680782Z",
        "is_active": true
    },
]
```
### Other Responses

1. **No school Found (204 No Content)**: 
 
   If there are no school in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No school found."
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


### 1. No School Found (204 No Content)
- **Message**: "No School found."
  - **Cause**: No School in the database or none meet the topper criteria.
  - **Solution**: Verify School data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 11. Teacher under the same department.

* `URL`: http://127.0.0.1:8000/teacher/teacherbydept/<int:dept_id>/

* `Method` : GET

* `Description`: It retrieves the list of teachers under the same department.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /teacher HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "emp_id": 16,
        "sc_id": 4,
        "department": [
            1,
            2,
            3,
            4
        ],
        "name": "Nithin Pillai",
        "performance": 0.0,
        "created_on": "2024-10-25T07:32:18.540701Z",
        "updated_on": "2024-11-03T18:32:10.752544Z",
        "is_active": true
    },
    {
        "emp_id": 2,
        "sc_id": 1,
        "department": [
            1,
            2
        ],
        "name": "Anjali Menon",
        "performance": 100.0,
        "created_on": "2024-10-25T07:32:18.480441Z",
        "updated_on": "2024-11-03T18:32:10.680782Z",
        "is_active": true
    },
    {
        "emp_id": 1,
        "sc_id": 1,
        "department": [
            1,
            2
        ],
        "name": "Anjali Menon",
        "performance": 100.0,
        "created_on": "2024-10-25T07:32:18.465411Z",
        "updated_on": "2024-11-03T18:32:10.674992Z",
        "is_active": true
    }
]
```
### Other Responses

1. **No teachers Found (204 No Content)**: 
 
   If there are no teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No teachers found."
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


### 1. No Teachers Found (204 No Content)
- **Message**: "No Teachers found."
  - **Cause**: No Teachers in the database or none meet the topper criteria.
  - **Solution**: Verify Teachers data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 12. Deactivate Teacher.

* `URL`: http://127.0.0.1:8000/teacher/teacherdeacivate/<int:emp_id>/

* `Method` : PUT

* `Description`: It inactivates teacher data.
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
    "message": "Teacher data set to inactive successfully"
}
```
### Other Responses

1. **No Teachers Found (204 No Content)**: 
 
   If there are no Teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No Teachers found."
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


### 1. No Teachers Found (204 No Content)
- **Message**: "No Teachers found."
  - **Cause**: No Teachers in the database or none meet the topper criteria.
  - **Solution**: Verify Teachers data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 13. Active Teachers.

* `URL`: http://127.0.0.1:8000/teacher/activeteachers/

* `Method` : GET

* `Description`: It retrieves the list of active teachers.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /teachers HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "emp_id": 1,
        "sc_id": 1,
        "department": [
            1,
            2
        ],
        "name": "Anjali Menon",
        "performance": 100.0,
        "created_on": "2024-10-25T07:32:18.465411Z",
        "updated_on": "2024-11-03T18:32:10.674992Z",
        "is_active": true
    },
    {
        "emp_id": 2,
        "sc_id": 1,
        "department": [
            1,
            2
        ],
        "name": "Anjali Menon",
        "performance": 100.0,
        "created_on": "2024-10-25T07:32:18.480441Z",
        "updated_on": "2024-11-03T18:32:10.680782Z",
        "is_active": true
    },
]
```
### Other Responses

1. **No Teachers Found (204 No Content)**: 
 
   If there are no teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No teachers found."
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


### 1. No Teachers Found (204 No Content)
- **Message**: "No teachers found."
  - **Cause**: No teachers in the database or none meet the topper criteria.
  - **Solution**: Verify teachers data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 14. Inactive Teachers.

* `URL`: http://127.0.0.1:8000/teacher/inactiveteachers/

* `Method` : GET

* `Description`: It retrieves list of inactive teachers.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /teachers HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "emp_id": 10,
        "sc_id": 4,
        "department": [],
        "name": "Arunachalam Reddy",
        "performance": 0.0,
        "created_on": "2024-10-25T07:32:18.514697Z",
        "updated_on": "2024-11-03T18:32:10.723141Z",
        "is_active": false
    },
    {
        "emp_id": 13,
        "sc_id": 1,
        "department": [
            5,
            6,
            7
        ],
        "name": "Meera Mohan",
        "performance": 0.0,
        "created_on": "2024-10-25T07:32:18.527659Z",
        "updated_on": "2024-11-03T18:32:10.737876Z",
        "is_active": false
    },
    {
        "emp_id": 17,
        "sc_id": 5,
        "department": [
            8
        ],
        "name": "Gopika Nambiar",
        "performance": 0.0,
        "created_on": "2024-10-25T07:32:18.544568Z",
        "updated_on": "2024-11-03T18:32:10.757939Z",
        "is_active": false
    },
]
```
### Other Responses

1. **No Teachers Found (204 No Content)**: 
 
   If there are no Teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No Teachers found."
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


### 1. No Teachers Found (204 No Content)
- **Message**: "No Teachers found."
  - **Cause**: No Teachers in the database or none meet the topper criteria.
  - **Solution**: Verify Teachers data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.


# API Endpoints of Department app

## 1. Create Department

* `URL`: http://127.0.0.1:8000/dept/

* `Method` : POST

* `Description`: Adds a new department record.

* `Content-type`:
  
         Content-Type: application/json

* `Body Parameters`:

# Department Model

| Field        | Data Type    | Constraints               | Relationship                          | Description                                                      |
|--------------|--------------|---------------------------|---------------------------------------|------------------------------------------------------------------|
| `hod_name`   | Foreign Key  | Optional                 | Foreign Key to `Teacher2`             | The head of department, linked to a teacher.                     |
| `dept_name`  | string       | Required                 | -                                     | The name of the department.                                      |
| `dept_id`    | integer      | Primary Key, AutoField   | -                                     | A unique identifier for each department.                         |
| `created_on` | DateTime     | Auto-generated           | -                                     | The date and time when the department record was created.        |
| `updated_on` | DateTime     | Auto-updated             | -                                     | The date and time when the department record was last updated.   |
| `is_active`  | boolean      | Default = True           | -                                     | Indicates if the department record is active.                    |




### Example Request

```http
POST /department HTTP/1.1
Host: api.example.com
Content-Type: application/json

[
    {
    "hod_name":1,
    "dept_name":"Music"
}
]


```
### Example Reponse
1.` HTTP Status: 200 OK`
```
[
    "message:Department Details Added Successfully"
]
```

### Other Responses

---

### Possible Responses for Creating a New Teacher

1. **`201 Created`**

   **Description:** The department was successfully created.

   **Example:**
   ```json
   [
    "message:Department Details Added Successfully"
  ]
   ```

---

2. **`400 Bad Request - Missing or Invalid Fields`**

   **Description:** Some required fields are missing, have incorrect data types, or contain invalid values.

   **Possible Causes:**

   * Required fields like `name` or `hod_name` are missing.
   * Invalid data types (e.g., providing a string instead of a float for `performance`).
   * Values out of valid range (e.g., negative values for `performance`).

   **Example:**
   ```json
   {
       "error": "Bad Request",
       "message": "Field 'name' is required.",
       
       }

   ```

---


---



---

3. **`405 Method Not Allowed`**

   **Description:** The HTTP method used is not supported for this endpoint.

   **Possible Causes:**

   * Using an unsupported method like GET instead of POST.

   **Example:**
   ```json
   {
       "error": "Method Not Allowed",
       "message": "The requested method is not allowed for this resource."
   }
   ```

---

4. **`500 Internal Server Error`**

    **Description:** An unexpected server error occurred.

    **Possible Causes:**

    * Database issues, such as connection errors.
    * Unhandled server exceptions during the processing of the request.

    **Example:**
    ```json
    {
        "error": "Internal Server Error",
        "message": "An error occurred while processing the request. Please try again later."
    }
    ```

---

### Messages

Here’s a more concise version of the error responses for creating a teacher.

---

---

1. **Missing Required Fields**

   ```json
   {
       "name": [
           "This field is required."
       ],
       "hod_name": [
           "This field is required."
       ]
   }
   ```

---



---

2. **Invalid Data Type**

   ```json
   [
    {
        "hod_name": [
            "Incorrect type. Expected pk value, received str."
        ]
    }
  ]
   ```

---

---


---





## 2. Retrieve Department Details

* `URL`: http://127.0.0.1:8000/dept/

* `Method` : GET

* `Description`: Retrieves all the Department records.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /Department HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. 
```python
[
    {
        "dept_id": 1,
        "dept_name": "Computer Science",
        "hod_name": 1,
        "schools": [
            {
                "sc_id": 1,
                "sc_name": "St. Joseph's High School",
                "location": "Kochi, Kerala"
            },
            {
                "sc_id": 2,
                "sc_name": "Holy Cross School",
                "location": "Kottayam, Kerala"
            },
            {
                "sc_id": 3,
                "sc_name": "Govt. Higher Secondary School",
                "location": "Thiruvananthapuram, Kerala"
            },
            {
                "sc_id": 4,
                "sc_name": "Bharathiya Vidya Bhavan",
                "location": "Thrissur, Kerala"
            },
            {
                "sc_id": 6,
                "sc_name": "ABC School",
                "location": "Kakkanad"
            }
        ]
    },
]
```
### Other Responses

1. No Data Available

* HTTP Status: 200 OK

* Description: The request was successful, but no department records are available.

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
`Cause`: The request was successful, but there are no department records in the database.

`Solution`: No action needed, but you may want to add department records to the database.

2. Page Not Found
   
* `HTTP Status: 404 Not Found`
```python
{
  "detail": "Not found."
}

```

- **Cause**:
  - **Incorrect URL**: The requested URL doesn’t match any defined route.
  
  - **Resource Missing**: The specific item (e.g., teacher ID) doesn’t exist in the database.
  - **Routing Issue**: The route might not be properly defined in `urls.py`.

- **Solution**:
  - **Check URL**: Ensure the URL and any IDs are correct.
  - **Validate Resource**: Confirm the resource exists in the database.
  - **Review URL Config**: Verify the endpoint is correctly set up in `urls.py`. 

## 3. Retrieve department Details by id

* `URL`: http://127.0.0.1:8000/dept/byid/<int:dept_id>

* `Method` : GET

* `Description`: Retrieves  the department records by id.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /department HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "dept_id": 8,
    "dept_name": "Geology",
    "hod_name": 7,
    "schools": [
        {
            "sc_id": 2,
            "sc_name": "Holy Cross School",
            "location": "Kottayam, Kerala"
        },
        {
            "sc_id": 3,
            "sc_name": "Govt. Higher Secondary School",
            "location": "Thiruvananthapuram, Kerala"
        }
    ]
}
```
### Other Responses

### 1. **Department Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The Department with the specified id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "Department not found."
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "dept_id must be a valid integer."
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

### 1. **Successful Retrieval of Department Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "dept_id": 8,
    "dept_name": "Geology",
    "hod_name": 7,
    "schools": [
        {
            "sc_id": 2,
            "sc_name": "Holy Cross School",
            "location": "Kottayam, Kerala"
        },
        {
            "sc_id": 3,
            "sc_name": "Govt. Higher Secondary School",
            "location": "Thiruvananthapuram, Kerala"
        }
    ]
  }
  ```

### 2. **Department Not Found**

  ```json
  {
    "error": "Department not found."
}
  ```
- **Cause**: The ID provided does not match any existing Department record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing Department.

### 3. **Bad Request**
- **Response Message**:
  ```json
  {
    "error": "Bad Request",
    "message": "dept_id must be a valid integer."
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

## 4. Update Department Details

* `URL`: http://127.0.0.1:8000/dept/byid/<int:dept_id>

* `Method` : PUT

* `Description`: Update Department details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /Department HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    "Department Details updated successfully"
]
```
### Other Responses

### 1. **Department Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The Department with the specified emp_id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "Department not found"
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the emp_id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "dept_id must be a valid integer."
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

### 1. **Successful Retrieval of Department Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  [
    "Department Details updated successfully"
  ]
  ```

### 2. **Department Not Found**

  ```json
  {
    "error": "Department not found"
}
  ```
- **Cause**: The ID provided does not match any existing Department record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing Department.

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


## 5. Delete Department Details

* `URL`: http://127.0.0.1:8000/dept/byid/<int:dept_id>

* `Method` : DELETE

* `Description`: Delete Department details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
DELETE /Department HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    "Department details deleted successfully"
]
```
### Other Responses

### 1. **Department Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The Department with the specified dept_id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "Department not found"
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the dept_id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "dept_id must be a valid integer."
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

### 1. **Successful Retrieval of Department Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "message": 
    "Department data deleted successfully"
   }
  ```

### 2. **Department Not Found**

  ```json
  {
    "error": "Department not found"
}
  ```
- **Cause**: The ID provided does not match any existing Department record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing Department.

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



## 6. Deactivate Department.

* `URL`: http://127.0.0.1:8000/dept/deactivatedept/<int:dept_id>/

* `Method` : PUT

* `Description`: It inactivates department data.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /department HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "message": "Department data set to inactive successfully"
}
```
### Other Responses

1. **No Department Found (204 No Content)**: 
 
   If there are no Department in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No Department found."
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


### 1. No Department Found (204 No Content)
- **Message**: "No Department found."
  - **Cause**: No Department in the database or none meet the topper criteria.
  - **Solution**: Verify Department data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 7. Active Department.

* `URL`: http://127.0.0.1:8000/dept/activedept/
* `Method` : GET

* `Description`: It retrieves the list of active departments.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /departments HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "dept_id": 1,
        "dept_name": "Computer Science",
        "hod_name": 1,
        "schools": [
            {
                "sc_id": 1,
                "sc_name": "St. Joseph's High School",
                "location": "Kochi, Kerala"
            },
            {
                "sc_id": 2,
                "sc_name": "Holy Cross School",
                "location": "Kottayam, Kerala"
            },
            {
                "sc_id": 3,
                "sc_name": "Govt. Higher Secondary School",
                "location": "Thiruvananthapuram, Kerala"
            },
            {
                "sc_id": 4,
                "sc_name": "Bharathiya Vidya Bhavan",
                "location": "Thrissur, Kerala"
            },
            {
                "sc_id": 6,
                "sc_name": "ABC School",
                "location": "Kakkanad"
            }
        ]
    },
    {
        "dept_id": 2,
        "dept_name": "Mechanical Engineering",
        "hod_name": 2,
        "schools": [
            {
                "sc_id": 1,
                "sc_name": "St. Joseph's High School",
                "location": "Kochi, Kerala"
            },
            {
                "sc_id": 2,
                "sc_name": "Holy Cross School",
                "location": "Kottayam, Kerala"
            },
            {
                "sc_id": 3,
                "sc_name": "Govt. Higher Secondary School",
                "location": "Thiruvananthapuram, Kerala"
            },
            {
                "sc_id": 4,
                "sc_name": "Bharathiya Vidya Bhavan",
                "location": "Thrissur, Kerala"
            }
        ]
    },
    {
        "dept_id": 14,
        "dept_name": "music",
        "hod_name": 3,
        "schools": []
    }
]
```
### Other Responses

1. **No Departments Found (204 No Content)**: 
 
   If there are no Departments in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No Departments found."
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


### 1. No Departments Found (204 No Content)
- **Message**: "No Departments found."
  - **Cause**: No Departments in the database 
  - **Solution**: Verify Departments data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 8. Inactive Departments.

* `URL`: http://127.0.0.1:8000/dept/inactivedept/

* `Method` : GET

* `Description`: It retrieves list of inactive departments.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /departments HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "dept_id": 3,
        "dept_name": "Sociology",
        "hod_name": 3,
        "schools": [
            {
                "sc_id": 2,
                "sc_name": "Holy Cross School",
                "location": "Kottayam, Kerala"
            },
            {
                "sc_id": 3,
                "sc_name": "Govt. Higher Secondary School",
                "location": "Thiruvananthapuram, Kerala"
            }
        ]
    },
    {
        "dept_id": 4,
        "dept_name": "Zoology",
        "hod_name": 4,
        "schools": 
            {
                "sc_id": 2,
                "sc_name": "Holy Cross School",
                "location": "Kottayam, Kerala"
            },
            {
                "sc_id": 3,
                "sc_name": "Govt. Higher Secondary School",
                "location": "Thiruvananthapuram, Kerala"
          }
    }
]
    
```
### Other Responses

1. **No Teachers Found (204 No Content)**: 
 
   If there are no Teachers in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No Teachers found."
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


### 1. No Teachers Found (204 No Content)
- **Message**: "No Teachers found."
  - **Cause**: No Teachers in the database or none meet the topper criteria.
  - **Solution**: Verify Teachers data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.





# API Endpoints of School app

## 1. Create School

* `URL`: http://127.0.0.1:8000/school/

* `Method` : POST

* `Description`: Adds a new school record.

* `Content-type`:
  
         Content-Type: application/json

* `Body Parameters`:

# School Model

| Field          | Data Type    | Constraints             | Relationship                                 | Description                                                     |
|----------------|--------------|-------------------------|----------------------------------------------|-----------------------------------------------------------------|
| `sc_name`      | string       | Required                | -                                            | The name of the school.                                       |
| `location`     | string       | Required                | -                                            | The location of the school.                                   |
| `sc_id`        | integer      | Primary Key, AutoField  | -                                            | A unique identifier for each school.                          |
| `created_on`   | DateTime     | Auto-generated          | -                                            | The date and time when the school record was created.         |
| `updated_on`   | DateTime     | Auto-updated            | -                                            | The date and time when the school record was last updated.    |
| `is_active`    | boolean      | Default = True          | -                                            | Indicates if the school record is active.                     |
| `departments`  | ManyToMany   | -                       | ManyToManyField to `Departments`            | The departments associated with the school.                   |
| `objects`      | Manager      | -                       | -                                            | The default manager for the model.                            |
| `active_objects`| Manager     | -                       | -                                            | Custom manager for querying active schools only.              |
             |




### Example Request

```http
POST /school HTTP/1.1
Host: api.example.com
Content-Type: application/json

[
    {
    "sc_name":"xyz",
    "location":"kochi",
    "departments":[1]
    }
]


```
### Example Reponse
1.` HTTP Status: 200 OK`
```
[
    "message:School Details Added Successfully"
]
```

### Other Responses

---

### Possible Responses for Creating a New Teacher

1. **`201 Created`**

   **Description:** The school was successfully created.

   **Example:**
   ```json
   [
    "message:School Details Added Successfully"
  ]
   ```

---

2. **`400 Bad Request - Missing or Invalid Fields`**

   **Description:** Some required fields are missing, have incorrect data types, or contain invalid values.

   **Possible Causes:**

   * Required fields like `sc_name` or `departments` are missing.
   * Invalid data types 
   * Values out of valid range 
   **Example:**
   ```json
   {
       "error": "Bad Request",
       "message": "Field 'sc_name' is required.",
       
       }

   ```

---


---



---

3. **`405 Method Not Allowed`**

   **Description:** The HTTP method used is not supported for this endpoint.

   **Possible Causes:**

   * Using an unsupported method like GET instead of POST.

   **Example:**
   ```json
   {
       "error": "Method Not Allowed",
       "message": "The requested method is not allowed for this resource."
   }
   ```

---

4. **`500 Internal Server Error`**

    **Description:** An unexpected server error occurred.

    **Possible Causes:**

    * Database issues, such as connection errors.
    * Unhandled server exceptions during the processing of the request.

    **Example:**
    ```json
    {
        "error": "Internal Server Error",
        "message": "An error occurred while processing the request. Please try again later."
    }
    ```

---

### Messages

Here’s a more concise version of the error responses for creating a teacher.

---

---

1. **Missing Required Fields**

   ```json
   {
       "sc_name": [
           "This field is required."
       ],
       "departments": [
           "This field is required."
       ]
   }
   ```

---



---

2. **Invalid Data Type**

   ```json
   [
    {
        "departments": [
            "Expected a list of items but got type \"int\"."
        ]
    }
  ]
   ```

---

---


---





## 2. Retrieve School Details

* `URL`: http://127.0.0.1:8000/school/

* `Method` : GET

* `Description`: Retrieves all the School records.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /School HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. 
```python
[
    {
        "sc_id": 1,
        "sc_name": "St. Joseph's High School",
        "location": "Kochi, Kerala",
        "created_on": "2024-10-25T06:37:25.834657Z",
        "updated_on": "2024-11-02T04:30:17.041044Z",
        "is_active": true,
        "departments": [
            1,
            2
        ]
    },
    {
        "sc_id": 2,
        "sc_name": "Holy Cross School",
        "location": "Kottayam, Kerala",
        "created_on": "2024-10-25T06:37:25.842300Z",
        "updated_on": "2024-10-25T06:37:25.842300Z",
        "is_active": true,
        "departments": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
        ]
    },
]
```
### Other Responses

1. No Data Available

* HTTP Status: 200 OK

* Description: The request was successful, but no school records are available.

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
`Cause`: The request was successful, but there are no school records in the database.

`Solution`: No action needed, but you may want to add school records to the database.

2. Page Not Found
   
* `HTTP Status: 404 Not Found`
```python
{
  "detail": "Not found."
}

```

- **Cause**:
  - **Incorrect URL**: The requested URL doesn’t match any defined route.
  
  - **Resource Missing**: The specific item (e.g.,sc_ID) doesn’t exist in the database.
  - **Routing Issue**: The route might not be properly defined in `urls.py`.

- **Solution**:
  - **Check URL**: Ensure the URL and any IDs are correct.
  - **Validate Resource**: Confirm the resource exists in the database.
  - **Review URL Config**: Verify the endpoint is correctly set up in `urls.py`. 

## 3. Retrieve school Details by id

* `URL`: http://127.0.0.1:8000/school/byid/<int:sc_id>

* `Method` : GET

* `Description`: Retrieves  the school records by id.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /school HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "sc_id": 1,
    "sc_name": "St. Joseph's High School",
    "location": "Kochi, Kerala",
    "created_on": "2024-10-25T06:37:25.834657Z",
    "updated_on": "2024-11-02T04:30:17.041044Z",
    "is_active": true,
    "departments": [
        1,
        2
    ]
}
```
### Other Responses

### 1. **School Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The School with the specified id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "School not found."
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "sc_id must be a valid integer."
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

### 1. **Successful Retrieval of School Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "sc_id": 1,
    "sc_name": "St. Joseph's High School",
    "location": "Kochi, Kerala",
    "created_on": "2024-10-25T06:37:25.834657Z",
    "updated_on": "2024-11-02T04:30:17.041044Z",
    "is_active": true,
    "departments": [
        1,
        2
    ]
  }
  ```

### 2. **School Not Found**

  ```json
  {
    "error": "School not found."
}
  ```
- **Cause**: The ID provided does not match any existing School record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing School.

### 3. **Bad Request**
- **Response Message**:
  ```json
  {
    "error": "Bad Request",
    "message": "sc_id must be a valid integer."
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

## 4. Update School Details

* `URL`: http://127.0.0.1:8000/school/byid/<int:sc_id>

* `Method` : PUT

* `Description`: Update School details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /School HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    "School Details updated successfully"
]
```
### Other Responses

### 1. **School Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The School with the specified emp_id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "School not found"
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the sc_id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "sc_id must be a valid integer."
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

### 1. **Successful Retrieval of School Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  [
    "School Details updated successfully"
  ]
  ```

### 2. **School Not Found**

  ```json
  {
    "error": "School not found"
}
  ```
- **Cause**: The ID provided does not match any existing School record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing School.

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


## 5. Delete School Details

* `URL`: http://127.0.0.1:8000/school/byid/<int:sc_id>

* `Method` : DELETE

* `Description`: Delete School details.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
DELETE /School HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    "School details deleted successfully"
]
```
### Other Responses

### 1. **School Not Found**

   - **HTTP Status**: `404 Not Found`
   - **Description**: The School with the specified sc_id does not exist.
   - **Example Response**:
     ```json
     {
    "error": "School not found"
  }
     ```

### 2. **Bad Request**

   - **HTTP Status**: `400 Bad Request`
   - **Description**: The request is malformed or the sc_id format is incorrect.
   - **Example Response**:
     ```json
     {
       "error": "Bad Request",
       "message": "sc_id must be a valid integer."
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

### 1. **Successful Retrieval of School Details**

- **HTTP Status**: `200 OK`
- **Response Message**:
  ```json
  {
    "message": 
    "School data deleted successfully"
   }
  ```

### 2. **School Not Found**

  ```json
  {
    "error": "School not found"
}
  ```
- **Cause**: The ID provided does not match any existing School record.
- **Solution**: Check the ID used in the request and ensure it corresponds to an existing School.

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



## 6. Deactivate School.

* `URL`: http://127.0.0.1:8000/school/deactivateschool//<int:sc_id>/

* `Method` : PUT

* `Description`: It inactivates school data.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
PUT /school HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
{
    "message": "school data set to inactive successfully"
}
```
### Other Responses

1. **No school Found (204 No Content)**: 
 
   If there are no school in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No school found."
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


### 1. No school Found (204 No Content)
- **Message**: "No school found."
  - **Cause**: No school in the database or none meet the topper criteria.
  - **Solution**: Verify school data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 7. Active school.

* `URL`: http://127.0.0.1:8000/school/activeschool/
  
* `Method` : GET

* `Description`: It retrieves the list of active school.

* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /school HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "sc_id": 1,
        "sc_name": "St. Joseph's High School",
        "location": "Kochi, Kerala",
        "created_on": "2024-10-25T06:37:25.834657Z",
        "updated_on": "2024-11-02T04:30:17.041044Z",
        "is_active": true,
        "departments": [
            1,
            2
        ]
    },
    {
        "sc_id": 2,
        "sc_name": "Holy Cross School",
        "location": "Kottayam, Kerala",
        "created_on": "2024-10-25T06:37:25.842300Z",
        "updated_on": "2024-10-25T06:37:25.842300Z",
        "is_active": true,
        "departments": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
        ]
    },
```
### Other Responses

1. **No School Found (204 No Content)**: 
 
   If there are no School in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No School found."
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


### 1. No School Found (204 No Content)
- **Message**: "No School found."
  - **Cause**: No School in the database 
  - **Solution**: Verify School data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.

## 8. Inactive School.

* `URL`: http://127.0.0.1:8000/school/inactiveschool/

* `Method` : GET

* `Description`: It retrieves list of inactive school.
* `Content-type`:
  
         Content-Type: application/json


### Example Request

```http
GET /School HTTP/1.1
Host: api.example.com
Content-Type: application/json
```
### Example Reponse
1. HTTP Status: 200 OK
```python
[
    {
        "sc_id": 8,
        "sc_name": "xyz",
        "location": "kochi",
        "created_on": "2024-11-03T19:27:38.825167Z",
        "updated_on": "2024-11-03T19:27:38.825167Z",
        "is_active": false,
        "departments": [
            1
        ]
    }
]
```
### Other Responses

1. **No School Found (204 No Content)**: 
 
   If there are no School in the database, you might choose to return a 204 status, indicating that the request was successful but there is no content to return.
   ```json
   {
       "status": "success",
       "message": "No School found."
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


### 1. No School Found (204 No Content)
- **Message**: "No School found."
  - **Cause**: No School in the database 
  - **Solution**: Verify School data or check selection criteria.

### 2. Bad Request (400 Bad Request)
- **Message**: "Invalid request parameters."
  - **Cause**: Malformed request or invalid parameters.
  - **Solution**: Check the API documentation for correct parameters.

### 3. Internal Server Error (500 Internal Server Error)
- **Message**: "An internal server error occurred. Please try again later."
  - **Cause**: Unexpected server-side issue.
  - **Solution**: Review server logs and contact the development team if needed.



