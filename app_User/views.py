from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from app_User.models import Users
from app_User.serializers import Userserializers
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


class UsercreateView(APIView):
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