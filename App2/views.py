from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
# Create your views here.
from .utils import calculate_average_marks,get_subjectwise_failed,calculate_teacher_pass_percentage

class Student1View(APIView):
    def get(self,request):
        students1=Student1.objects.all()
        serializer=Student1serializers(students1, many=True)
        return Response(serializer.data)

    def delete(self,request):
        try:
            students1=Student1.objects.all()
            # name=students1.name
            students1.delete()
            return Response({'Student record deleted successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        serialize=Student1serializers(data=request.data,many=True)
        if serialize.is_valid():
            serialize.save()
            return Response({"message:""Student Details Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

class Student1DetailView(APIView):
    def get(self,request,rollno):
        students1=Student1.objects.get(rollno=rollno)
        serializer=Student1serializers(students1)
        return Response(serializer.data)
    
    def put(self,request,rollno):
        students1=Student1.objects.get(rollno=rollno)
        serializer=Student1serializers(students1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,rollno):
        try:
            students1=Student1.objects.get(rollno=rollno)
            name=students1.name
            students1.delete()
            return Response({'Student record deleted successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Student1Listtoppers(APIView):
    def get(self,request):
        students1 = Student1.objects.all().order_by('-total_marks')[:5]
        serializer=Student1serializers(students1,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class Student1LitofcutoffsView(APIView):
    def get(self,request):
        students1=Student1.objects.filter(total_marks__gt=150)
        serializer=Student1serializers(students1,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Student1ListofFailedView(APIView):
    def get(self,request):
        students1=Student1.objects.filter(total_marks__lte=150)
        serializer=Student1serializers(students1,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    

class Student1ListofaverageView(APIView):
    def get(self, request):
        students1 = Student1.objects.all()
        average_marks = calculate_average_marks(students1.count(), sum(student.total_marks for student in students1))
        above_average = Student1.objects.filter(total_marks__gte=average_marks)
        below_average = Student1.objects.filter(total_marks__lt=average_marks)
        return Response({
            'average_marks': average_marks,
            'students_above_average': Student1serializers(above_average, many=True).data,
            'students_below_average': Student1serializers(below_average, many=True).data
        }, status=status.HTTP_200_OK)


class StudentsubjectwisefailedlistView(APIView):
    def get(self,request):
        cutoff_marks=50
        subjectwise_failures= get_subjectwise_failed(cutoff_marks)
        return Response({
            'failedin_maths':Student1serializers(subjectwise_failures['failedin_maths'],many=True).data,
            'failedin_chemistry':Student1serializers(subjectwise_failures['failedin_chemistry'],many=True).data,
            'failedin_physics':Student1serializers(subjectwise_failures['failedin_physics'],many=True).data
        },status=status.HTTP_200_OK) 


class TeacherPerformanceView(APIView):
    def get(self, request):
        best_teachers = []
        teachers_needing_improvement = []
        teachers = Teacher.objects.all()
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
            teacher = Teacher.objects.get(emp_id=teacher_id) #fetching the teacher object
            teacher_serializer = Teacherserializers(teacher)#serializing teacher data
            return Response({
                'teacher': teacher_serializer.data
                # 'students': student_list
            }, status=status.HTTP_200_OK)

        except Teacher.DoesNotExist:
            return Response({
                'error': 'Teacher not found.'
            }, status=status.HTTP_404_NOT_FOUND)



class TeacherallDetailsView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = Teacherserializers(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Teacherserializers(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Teacher details added successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors so you can debug issues
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request):
        teachers=Teacher.objects.all()
        teachers.delete()
        return Response({'Teacher record deleted successfully'},status=status.HTTP_200_OK)


class updateperformanceView(APIView):
    def post(self, request):
        serializer = Student1serializers(data=request.data)  # Use without many=True for a single instance
        
        if serializer.is_valid():
            student = serializer.save()  # This will return a single Student1 instance

            if student.teacher_id:
                teacher_id = student.teacher_id.emp_id
                new_pass_percentage = calculate_teacher_pass_percentage(teacher_id)
                teacher = Teacher.objects.get(emp_id=teacher_id)
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
            teacher=Teacher.objects.get(emp_id=teacher_id)
            teacher.performance=new_pass_percentage
            teacher.save()
            return Response({"message": f"Student {student.name} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except Student1.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        except Teacher.DoesNotExist:
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
                    teacher = Teacher.objects.get(emp_id=teacher_id)
                    teacher.performance = calculate_teacher_pass_percentage(teacher_id)
                    teacher.save()

                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response({"error": "No associated teacher."}, status=status.HTTP_400_BAD_REQUEST)
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except (Student1.DoesNotExist, Teacher.DoesNotExist):
            return Response({"error": "Student or Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
