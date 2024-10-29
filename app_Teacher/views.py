from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from App2.models import Student1
from app_Teacher.models import Teacher2
from app_Teacher.serializers import *
from App2.serializers import Student1serializers
from App2.utils import calculate_teacher_pass_percentage

# Create your views here.
class TeachercreateView(APIView):
    #fetching teacher record
    def get(self, request):
        teachers = Teacher2.objects.all()
        serializer = Teacher2serializers(teachers, many=True)
        return Response(serializer.data)

    # creating teacher record
    def post(self, request):
        serializer = Teacher2serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Teacher details added successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors so you can debug issues
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TeacherdetailsView(APIView):
    #fetching teacher record by teacher id
    def get(self, request, teacher_id):
        try:
            teacher = Teacher2.objects.get(emp_id=teacher_id) #fetching the teacher object
            teacher_serializer = Teacher2serializers(teacher)#serializing teacher data
            return Response({'teacher': teacher_serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': 'Teacher not found.'}, status=status.HTTP_204_NO_CONTENT)

    #updating teacher data by id
    def put(self,request,emp_id):
        try:
            teacher=Teacher2.active_objects.get(emp_id=emp_id)
        except Teacher2.Doesnotexist:
            return Response({"error":"Teacher not found"},status=status.HTTP_204_NO_CONTENT)
        serializer=Teacher2serializers(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete teacher details by id
    def delete(self, request, emp_id):
        try:
            # Corrected typo: 'Tracher2' should be 'Teacher2'
            teacher = Teacher2.active_objects.get(emp_id=emp_id)
            teacher.delete()
            return Response({'message': "Teacher data deleted successfully"}, status=status.HTTP_200_OK)
        except Teacher2.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=status.HTTP_204_NO_CONTENT)



class TeacherPerformanceView(APIView):
    # finding the performance of teacher
    def get(self, request):
        best_teachers = []
        teachers_needing_improvement = []
        teachers = Teacher2.objects.all()
        for teacher in teachers:
                pass_percentage= calculate_teacher_pass_percentage(teacher.emp_id)
                if pass_percentage >= 75:
                    best_teachers.append({'teacher_name': teacher.name,'pass_percentage': pass_percentage})
                else: 
                    teachers_needing_improvement.append({
                        'teacher_name': teacher.name,
                        'pass_percentage': pass_percentage
                    })

        return Response({'best_teachers': best_teachers,'teachers_needing_improvement': teachers_needing_improvement
        }, status=status.HTTP_200_OK)



class UpdateperbyaddView(APIView):
    #update performance by adding new student
    def post(self, request):
        serializer = Student1serializers(data=request.data)  # No need for many=True with a single instance
        
        if serializer.is_valid():
            student = serializer.save()  # Save and return the Student1 instance

            if student.teacher_id:
                # Calculate the new performance
                teacher = student.teacher_id
                teacher.performance = calculate_teacher_pass_percentage(teacher.emp_id)
                teacher.save()  # Update performance in one DB call
            else:
                return Response(
                    {"error": f"Student {student.name} has no associated teacher."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {"message": f"Student {student.name} details added successfully, and teacher performance updated."},
                status=status.HTTP_201_CREATED
            )
        # Return validation errors if serializer is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateperbydelView(APIView):
    # update performance by deleting student record
    def delete(self, request, rollno):
        try:
        # Attempt to fetch the student and related teacher in one step
            student = Student1.objects.select_related('teacher_id').get(rollno=rollno)
        # Delete the student and update the teacher's performance
            teacher = student.teacher_id
            student_name = student.name  # Store student name before deletion
            student.delete()
        # Recalculate and update the teacher's performance
            teacher.performance = calculate_teacher_pass_percentage(teacher.emp_id)
            teacher.save()
            return Response(
            {"message": f"Student {student_name} deleted successfully."}, 
            status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #update performance by updating the student data
    def put(self, request, rollno):
        try:
            student = Student1.objects.get(rollno=rollno)
            serializer = Student1serializers(student, data=request.data)
            if serializer.is_valid():
                serializer.save()  # Save the updated student details
                if student.teacher_id:  # Ensure the student has an associated teacher
                    teacher_id = student.teacher_id.emp_id
                    teacher = Teacher2.objects.get(emp_id=teacher_id)
                    teacher.performance = calculate_teacher_pass_percentage(teacher_id)
                    teacher.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response({"error": "No associated teacher."}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (Student1.DoesNotExist, Teacher2.DoesNotExist):
            return Response({"error": "Student or Teacher not found."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Teacher under the same school
class Teacherbyschoolview(APIView):
    def get(self,request,sc_id):
        teacher=Teacher2.active_objects.filter(sc_id=sc_id)
        serializer=Teacher2serializers(teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# active teachers
class Activeteachers(APIView):
    def get(self,request):
        teacher=Teacher2.active_objects.all()
        serializer=Teacher2serializers(teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#inactive teachers
class Inactiveteachers(APIView):
    def get(self,request):
        teacher=Teacher2.objects.filter(is_active=False)
        serializer=Teacher2serializers(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# teachers under the same dept
class Teacherbydeptview(APIView):
    def get(self,request,dept_id):
        teacher=Teacher2.active_objects.filter(dept_id=dept_id)
        serializer=Teacher2serializers(teacher,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#deactivate teacher data   
class TeacherdeactivateView(APIView):
    def put(self, request, emp_id):
        try:
            teacher = Teacher2.objects.filter(emp_id=emp_id).update(emp_id=None,is_active=False)
            if teacher==0:
                return Response({"error": "Teacher not found"}, status=status.HTTP_204_NO_CONTENT)
            return Response({'message': "Teacher data set to inactive successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
