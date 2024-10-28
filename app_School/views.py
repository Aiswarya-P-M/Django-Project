from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import School
from .serializers import SchoolSerializer
from app_Department.models import Departments
from app_Teacher.models import Teacher2
from App2.models import Student1

class SchoolcreateView(APIView):
    # fetching all the school details
    def get(self,request):
        schools=School.objects.all()
        serializer=SchoolSerializer(schools,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # creating school details
    def post(self,request):
        serializer=SchoolSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message:""School Details Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #deleting all the school details
    # def delete(self,request):
    #     try:
    #         school=School.objects.all()
    #         school.delete()
    #         return Response({'School details deleted successfully'},status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            schools = School.objects.all()
            for school in schools:
                school.is_active = False
                school.save()

                # Inactivate related departments, teachers, and students
                departments = Departments.objects.filter(sc_id=school.sc_id)
                departments.update(is_active=False)
                
                teachers = Teacher2.objects.filter(sc_id=school.sc_id)
                teachers.update(is_active=False)
                
                students = Student1.objects.filter(sc_id=school.sc_id)
                students.update(is_active=False)
                
            return Response({'School details set to inactive successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class  SchooldetailsView(APIView):
    # fetching the school details by id
    def get(self,request,sc_id):
        try:
            school=School.objects.get(sc_id=sc_id)
            serializer=SchoolSerializer(school)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"School not found"}, status=status.HTTP_404_NOT_FOUND)
    # updating the school details by id
    def put(self,request,sc_id):
            school=School.objects.get(sc_id=sc_id)
            serializer=SchoolSerializer(school,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"School Details updated successfully"},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    # deleting the school details by id
    # def delete(self,request,sc_id):
    #     try:
    #         school=School.objects.get(sc_id=sc_id)
    #         school.delete()
    #         return Response({"School details deleted successfully"}, status=status.HTTP_200_OK)
    #     except:
    #         return Response({"error":"School not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, sc_id):
        try:
            school = School.objects.get(sc_id=sc_id)
            school.is_active = False
            school.save()

            # Inactivate related departments, teachers, and students
            Departments.objects.filter(sc_id=sc_id).update(is_active=False)
            Teacher2.objects.filter(sc_id=sc_id).update(is_active=False)
            Student1.objects.filter(sc_id=sc_id).update(is_active=False)
            
            return Response({"message": "School and associated records set to inactive successfully"}, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND) 


class ActiveSchoolView(APIView):
    def get(self, request):
        try:
            # Use filter instead of get to allow multiple active departments
            school = School.active_objects.filter(is_active=True)
            serializer = SchoolSerializer(school, many=True)  # many=True for multiple objects
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_400_BAD_REQUEST)

class InactiveSchoolView(APIView):
    def get(self, request):
        # Use filter to get all inactive departments
        school = School.objects.filter(is_active=False)
        serializer = SchoolSerializer(school, many=True)  # many=True for multiple objects
        
        # If no inactive departments are found, return an empty list
        return Response(serializer.data, status=status.HTTP_200_OK)  
        
    