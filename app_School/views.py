from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import School
from .serializers import SchoolSerializer

class SchoolcreateView(APIView):
    def get(self,request):
        schools=School.objects.all()
        serializer=SchoolSerializer(schools,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=SchoolSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message:""School Details Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request):
        try:
            school=School.objects.all()
            school.delete()
            return Response({'School details deleted successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class  SchooldetailsView(APIView):
    def get(self,request,sc_id):
        try:
            school=School.objects.get(sc_id=sc_id)
            serializer=SchoolSerializer(school)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"School not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,sc_id):
            school=School.objects.get(sc_id=sc_id)
            serializer=SchoolSerializer(school,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"School Details updated successfully"},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(self,request,sc_id):
        try:
            school=School.objects.get(sc_id=sc_id)
            school.delete()
            return Response({"School details deleted successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"School not found"}, status=status.HTTP_404_NOT_FOUND)        
        
    