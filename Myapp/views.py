from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
# Create your views here.

class StudentView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=Studentserializers(students, many=True)
        return Response(serializer.data)


    def post(self,request):
        serialize=Studentserializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)