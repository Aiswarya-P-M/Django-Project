from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Departments
from .serializers import DeptSerializer

class DeptcreateView(APIView):
    def get(self,request):
        dept=Departments.objects.all()
        serializer=DeptSerializer(dept,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=DeptSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message:""Department Details Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request):
        try:
            dept=Departments.objects.all()
            dept.delete()
            return Response({'Department details deleted successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class  DeptdetailsView(APIView):
    def get(self,request,dept_id):
        try:
            dept=Departments.objects.get(dept_id=dept_id)
            serializer=DeptSerializer(dept)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"Department not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,dept_id):
            dept=Departments.objects.get(dept_id=dept_id)
            serializer=DeptSerializer(dept,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Department Details updated successfully"},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self,request,dept_id):
        try:
            dept=Departments.objects.get(dept_id=dept_id)
            dept.delete()
            return Response({"Department details deleted successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"Department not found"}, status=status.HTTP_404_NOT_FOUND)        
        
    