from django.contrib.auth import authenticate
from django.contrib.auth.hashers import  make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_User.models import Users
from app_User.serializers import Userserializers
from rest_framework.authtoken.models import Token
from rest_framework import permissions
# Create your views here.


class UsercreateView(APIView):
    def post(self,request):
        serializer=Userserializers(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            token, created=Token.objects.get_or_create(user=user)
            return Response({
                "user":serializer.data,
                "token":token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    def get(self,request):
        users=Users.objects.all()
        serializer=Userserializers(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def delete(self, request):
        user=Users.objects.all()
        user.delete()
        return Response({"message":"User deleted successfully"}, status=status.HTTP_200_OK)


class UserOperationByID(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request, id):
        user=Users.objects.get(id=id)
        serializer=Userserializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        user=Users.objects.get(id=id)
        serializer=Userserializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        user=Users.objects.get(id=id)
        user.delete()
        return Response({"message":"User deleted successfully"}, status=status.HTTP_200_OK)


class LoginView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        print("username is", username)
        print("password is", password)
        hashed_password = make_password(password)
        print("hashed password is", hashed_password)
        user= authenticate(username=username,password=password)
        print("username is",user)
        if user is not None:
            token, created =Token.objects.get_or_create(user=user)
            return Response({"token":token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)


class LogOutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message":"Logged out successfully"}, status=status.HTTP_200_OK)
        except (AttributeError, KeyError):
            return Response({"details":"No active session to logout"}, status=status.HTTP_400_BAD_REQUEST)


