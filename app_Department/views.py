from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Departments
from .serializers import DeptSerializer
from app_Teacher.models import Teacher2
from App2.models import Student1

class DeptcreateView(APIView):
    # function for fetching all the details of department
    def get(self, request, dept_id):
        try:
            # Get the department by ID
            department = Departments.objects.get(dept_id=dept_id)
            # Serialize the department with associated schools
            serializer =DeptSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Departments.DoesNotExist:
            return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

    #function for creating department
    def post(self,request):
        serializer=DeptSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message:""Department Details Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class  DeptdetailsView(APIView):
    #function for fetching the details of particular department using the dept_id
    def get(self,request,dept_id):
        try:
            dept=Departments.objects.get(dept_id=dept_id)
            serializer=DeptSerializer(dept)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"Department not found"}, status=status.HTTP_204_NO_CONTENT)

    #function for updating the details of particular department using the dept_id
    def put(self,request,dept_id):
            dept=Departments.objects.get(dept_id=dept_id)
            serializer=DeptSerializer(dept,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Department Details updated successfully"},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
    #function for deleting the details of particular department using the dept_id
    def delete(self,request,dept_id):
        try:
            dept=Departments.objects.get(dept_id=dept_id)
            dept.delete()
            return Response({"Department details deleted successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"Department not found"}, status=status.HTTP_204_NO_CONTENT) 

class DeptdeactivateView(APIView):
    # function for inactivate department
    def put(self, request, dept_id):
        try:
            dept = Departments.objects.filter(dept_id=dept_id).update(is_active=False)
            if dept==0:
                return Response({"error": "Department not found"}, status=status.HTTP_204_NO_CONTENT)
            Teacher2.objects.filter(dept_id=dept_id).update(dept_id=None,is_active=False)
            Student1.objects.filter(dept_id=dept_id).update(dept_id=None,is_active=False)
            return Response({"Department details set to inactive successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ActivedeptView(APIView):
    # function for finding the active department
    def get(self, request):
        try:
            # Use filter instead of get to allow multiple active departments
            dept = Departments.active_objects.filter(is_active=True)
            serializer = DeptSerializer(dept, many=True)  # many=True for multiple objects
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Departments.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_400_BAD_REQUEST)

class InactiveDeptView(APIView):
    #function for fetching the inactive department
    def get(self, request):
        # Use filter to get all inactive departments
        dept = Departments.objects.filter(is_active=False)
        serializer = DeptSerializer(dept, many=True)  # many=True for multiple objects
        
        # If no inactive departments are found, return an empty list
        return Response(serializer.data, status=status.HTTP_200_OK)

