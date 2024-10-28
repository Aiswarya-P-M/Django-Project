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
        serialize=Student1serializers(data=request.data)
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
    
    # def delete(self,request,rollno):
    #     try:
    #         students1=Student1.objects.get(rollno=rollno)
    #         name=students1.name
    #         students1.delete()
    #         return Response({'Student record deleted successfully'},status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rollno):
        try:
            student = Student1.objects.get(rollno=rollno)
            student.is_active = False
            student.save()
            return Response({'Student record set to inactive successfully'}, status=status.HTTP_200_OK)
        except Student1.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

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

#is_active without using Active Manager

class StudentbydeptView(APIView):
    def get(self,request,dept_id):
        student=Student1.objects.filter(dept_id=dept_id,is_active=True)
        serializer=Student1serializers(student,many=True)
        data=[{
            'name':student['name'],
            'rollno':student['rollno'],
            'dept_id':student['dept_id'],
            'sc_id':student['sc_id']
        } for student in serializer.data
        ]
        return Response(data,status=status.HTTP_200_OK)

#is_active with using Active Manager
class Studentbydeptactview(APIView):
    def get(self,request,dept_id):
        student=Student1.active_objects.filter(dept_id=dept_id)
        serializer=Student1serializers(student,many=True)
        data=[{
            'name':student['name'],
            'rollno':student['rollno'],
            'dept_id':student['dept_id'],
            'sc_id':student['sc_id']
        } for student in serializer.data
        ]
        return Response(data,status=status.HTTP_200_OK)

# fetching the student details based on the school under the same school

class StudentbyscidView(APIView):
    def get(self,request,sc_id):
        student=Student1.active_objects.filter(sc_id=sc_id)
        serializer=Student1serializers(student,many=True)
        data=[{
            'name':student['name'],
            'rollno':student['rollno'],
            'dept_id':student['dept_id'],
            'sc_id':student['sc_id']
        } for student in serializer.data
        ]
        return Response(data,status=status.HTTP_200_OK)

class Studentunderteacher(APIView):
    def get(self, request, teacher_id):
        teacher = Teacher2.objects.filter(emp_id=teacher_id).first()
        if not teacher:
            return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        students = Student1.active_objects.filter(teacher_id=teacher_id)
        serializer = Student1serializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Studentunderdeptandschool(APIView):
    def get(self,request,dept_id,sc_id):
        student=Student1.active_objects.filter(dept_id=dept_id,sc_id=sc_id)
        serializer=Student1serializers(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ActivestudView(APIView):
    def get(self,request):
        stud=Student1.active_objects.all()
        serializer=Student1serializers(stud, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class InactivestudView(APIView):
    def get(self,request):
        stud=Student1.objects.filter(is_active=False)
        serializer=Student1serializers(stud,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
