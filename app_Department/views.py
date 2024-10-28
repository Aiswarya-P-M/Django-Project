from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Departments
from .serializers import DeptSerializer
from app_Teacher.models import Teacher2
from App2.models import Student1

class DeptcreateView(APIView):
    # function for fetching all the details of department
    def get(self,request):
        dept=Departments.objects.all()
        serializer=DeptSerializer(dept,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #function for creating department
    def post(self,request):
        serializer=DeptSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message:""Department Details Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #function for deleting all the details of department
    # def delete(self,request):
    #     try:
    #         dept=Departments.objects.all()
    #         dept.delete()
    #         return Response({'Department details deleted successfully'},status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
             #fetches all department records
            departments = Departments.objects.all()
            for dept in departments:
                #For each department, the is_active attribute is set to False
                dept.is_active = False
                dept.save()
                
                #inactivates all teachers and students associated with the current department
                Teacher2.objects.filter(dept_id=dept.dept_id).update(is_active=False)
                Student1.objects.filter(dept_id=dept.dept_id).update(is_active=False)
                
            return Response({'Department details set to inactive successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class  DeptdetailsView(APIView):
    #function for fetching the details of particular department using the dept_id
    def get(self,request,dept_id):
        try:
            dept=Departments.objects.get(dept_id=dept_id)
            serializer=DeptSerializer(dept)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"Department not found"}, status=status.HTTP_404_NOT_FOUND)
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

    # def delete(self,request,dept_id):
    #     try:
    #         dept=Departments.objects.get(dept_id=dept_id)
    #         dept.delete()
    #         return Response({"Department details deleted successfully"}, status=status.HTTP_200_OK)
    #     except:
    #         return Response({"error":"Department not found"}, status=status.HTTP_404_NOT_FOUND)        
        
    def delete(self, request, dept_id):
        try:
            dept = Departments.objects.get(dept_id=dept_id)
            dept.is_active = False
            dept.save()
            
            # Inactivate related teachers and students
            Teacher2.objects.filter(dept_id=dept_id).update(is_active=False)
            Student1.objects.filter(dept_id=dept_id).update(is_active=False)
            
            return Response({"Department details set to inactive successfully"}, status=status.HTTP_200_OK)
        except Departments.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

class ActivedeptView(APIView):
    def get(self, request):
        try:
            # Use filter instead of get to allow multiple active departments
            dept = Departments.active_objects.filter(is_active=True)
            serializer = DeptSerializer(dept, many=True)  # many=True for multiple objects
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Departments.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_400_BAD_REQUEST)

class InactiveDeptView(APIView):
    def get(self, request):
        # Use filter to get all inactive departments
        dept = Departments.objects.filter(is_active=False)
        serializer = DeptSerializer(dept, many=True)  # many=True for multiple objects
        
        # If no inactive departments are found, return an empty list
        return Response(serializer.data, status=status.HTTP_200_OK)

