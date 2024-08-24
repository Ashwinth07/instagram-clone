from datetime import datetime
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
import bcrypt

class UsersAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        data = users.values()
        return Response({"data": data})

class UserAPI(APIView):

    def __init__(self):
        self.user_auth = UserAuthentication()

    def post(self, request):
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        bio = request.query_params.get('bio', 'This is my bio')

        hashed_password, salt = self.user_auth.hash_password(password)

        user = User(username=username, password=hashed_password.decode('utf-8'), 
                    salt=salt.decode('utf-8'), email=email, bio=bio, 
                    last_login=datetime.now(), is_active=True, created_date=datetime.now())

        user.save()
        if user:
            return Response({"status": 200, "message": "Account created successfully"})
        else:
            return Response({"status": 500, "message": "Error while creating account"})

    def get(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')

        user = User.objects.filter(email=email).first()  # Use first() to get the first matching record

        if user:
            h_password = user.password.encode('utf-8')  # Convert the password back to bytes
            is_match = self.user_auth.check_password(password, h_password)
            if is_match:
                return Response({"status": 200, "is_user": True, "message": "Successfully logged in"})
            else:
                return Response({"status": 401, "is_user": False, "message": "Invalid credentials"})
        else:
            return Response({"status": 404, "is_user": False, "message": "User not found"})

class UserAuthentication:
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, salt)
        return hashed_password, salt

    def check_password(self, password, hashed_password):
        pass_bytes = password.encode('utf-8')
        is_password_match = bcrypt.checkpw(pass_bytes, hashed_password)
        return is_password_match
