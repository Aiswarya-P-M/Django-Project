from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from App2.models import Student1
from app_Teacher.models import Teacher2
from app_Teacher.serializers import *
from App2.serializers import Student1serializers
from App2.utils import calculate_teacher_pass_percentage

# Create your views here.
class TeacherPerformanceView(APIView):
    def get(self, request):
        best_teachers = []
        teachers_needing_improvement = []
        teachers = Teacher2.objects.all()
        for teacher in teachers:
                pass_percentage= calculate_teacher_pass_percentage(teacher.emp_id)
                if pass_percentage >= 75:
                    best_teachers.append({
                        'teacher_name': teacher.name,
                        'pass_percentage': pass_percentage 
                    })
                else: 
                    teachers_needing_improvement.append({
                        'teacher_name': teacher.name,
                        'pass_percentage': pass_percentage
                    })

        return Response({
            'best_teachers': best_teachers,
            'teachers_needing_improvement': teachers_needing_improvement
        }, status=status.HTTP_200_OK)

class teacherdetailsView(APIView):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher2.objects.get(emp_id=teacher_id) #fetching the teacher object
            teacher_serializer = Teacher2serializers(teacher)#serializing teacher data
            return Response({
                'teacher': teacher_serializer.data
                # 'students': student_list
            }, status=status.HTTP_200_OK)

        except Teacher2.DoesNotExist:
            return Response({
                'error': 'Teacher not found.'
            }, status=status.HTTP_404_NOT_FOUND)



class TeacherallDetailsView(APIView):
    def get(self, request):
        teachers = Teacher2.objects.all()
        serializer = Teacher2serializers(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Teacher2serializers(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Teacher details added successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors so you can debug issues
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request):
        teachers=Teacher2.objects.all()
        teachers.delete()
        return Response({'Teacher record deleted successfully'},status=status.HTTP_200_OK)


class updateperbyaddView(APIView):
    def post(self, request):
        serializer = Student1serializers(data=request.data)  # Use without many=True for a single instance
        
        if serializer.is_valid():
            student = serializer.save()  # This will return a single Student1 instance

            if student.teacher_id:
                teacher_id = student.teacher_id.emp_id
                new_pass_percentage = calculate_teacher_pass_percentage(teacher_id)
                teacher = Teacher2.objects.get(emp_id=teacher_id)
                teacher.performance = new_pass_percentage
                teacher.save()
            else:
                return Response({"error": f"Student {student.name} has no associated teacher."}, status=status.HTTP_400_BAD_REQUEST)

            # Return a success message
            return Response({"message": "Student details added successfully."}, status=status.HTTP_201_CREATED)

        # If validation fails, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class performanceupdateView(APIView):
    def delete(self,request,rollno):
        try:
            student=Student1.objects.get(rollno=rollno)
            teacher_id=student.teacher_id.emp_id
            student.delete()
            new_pass_percentage=calculate_teacher_pass_percentage(teacher_id)
            teacher=Teacher2.objects.get(emp_id=teacher_id)
            teacher.performance=new_pass_percentage
            teacher.save()
            return Response({"message": f"Student {student.name} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except Student1.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        except Teacher2.DoesNotExist:
            return Response({"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
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
            return Response({"error": "Student or Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
