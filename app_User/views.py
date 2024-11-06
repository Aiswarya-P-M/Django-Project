from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_User.models import Users
from app_User.serializers import Userserializers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UsercreateView(APIView):
    # permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=Userserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mesage":"User created successfully"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        users=Users.objects.all()
        serializer=Userserializers(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request):
        users=Users.objects.all()
        users.delete()
        return Response({"message":"All users deleted successfully"}, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self,request):
        username=request.data["username"]
        password=request.data["password"]
        print(username, password)
        user=authenticate(request,username=username,password=password)
        # print("username is",user.username)
        if user is not None:
            token,created=Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=status.HTTP_200_OK)
            # Response({"username":user.username},status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)

class ChangePasswordView(APIView):
    def put(self, request, *args, **kwargs):
        username = request.data.get("username")
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")

        # Fetch the user and validate credentials in one go
        user = Users.objects.filter(username=username).first()
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if not check_password(old_password, user.password):
            return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the new password
        if len(new_password) < 8:
            return Response({"error": "New password must be at least 8 characters long."}, status=status.HTTP_400_BAD_REQUEST)
        if new_password != confirm_password:
            return Response({"error": "New password and confirm password do not match."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the user's password
        user.password = make_password(new_password)
        user.save()

        return Response({"success": "Password updated successfully."}, status=status.HTTP_200_OK)

