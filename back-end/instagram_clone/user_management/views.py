from datetime import datetime
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comments, User
from .serilaizers import CommentSerializer

# Create your views here.
class CommentAPI(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        print(comments)
        data = CommentSerializer(comments)
        return Response(data.data)

class UsersAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        data = users.values()
        return Response({"data":data})
    
class UserAPI(APIView):
    def post(self, request):
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        bio = request.query_params.get('bio', 'This is my bio')

        user = User(username=username, password=password, email = email,
                     bio=bio, last_login = datetime.now(),
                     is_active=True, created_date = datetime.now())
        user.save()
        if user:
            return Response({"status":200, "message":"Account created successfully"})
        else:
            return Response({"status":500, "message":"Error while creating account"})

    def get(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        
        user = User.objects.filter(email=email, password=password)
        if user:
            return  Response({"status":200, "is_user":True})
        else:
            return  Response({"status":200, "is_user":False})
        
