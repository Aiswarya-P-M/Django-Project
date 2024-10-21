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
    
    def delete(self,request,rollno):
        try:
            students1=Student1.objects.get(rollno=rollno)
            name=students1.name
            students1.delete()
            return Response({'message':f'Student {name} deleted successfully'},status=status.HTTP_200_OK)
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
    def get(self,request):
        average_marks=calculate_average_marks()
        students_above_average=Student1.objects.filter(total_marks__gte=average_marks)
        students_below_average=Student1.objects.filter(total_marks__lt=average_marks)
        above_average_serializer=Student1serializers(students_above_average,many=True)
        below_average_serializer=Student1serializers(students_below_average,many=True)
        return Response({
            'average_marks': average_marks,
            'students_above_average': above_average_serializer.data,
            'students_below_average': below_average_serializer.data
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
        teachers = Student1.objects.values_list('classteacher', flat=True).distinct()
        for teacher_name in teachers:
                pass_percentage= calculate_teacher_pass_percentage(teacher_name)
                if pass_percentage >= 75:
                    best_teachers.append({
                        'teacher_name': teacher_name,
                        'pass_percentage': pass_percentage 
                    })
                else: 
                    teachers_needing_improvement.append({
                        'teacher_name': teacher_name,
                        'pass_percentage': pass_percentage
                    })

        return Response({
            'best_teachers': best_teachers,
            'teachers_needing_improvement': teachers_needing_improvement
        }, status=status.HTTP_200_OK)