from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import User

@api_view(["GET"])
def home(request):
    print("get request as been sent!!!!")
    return Response({"message":"This is some message"})

@api_view(["POST"])
def login(request):
    email = request.data["email"]
    password = request.data["password"]

    user = authenticate(request, username=email, password=password)

    if email and password:
        # TBD: login the user
        print(email, password)
        return Response({'message': 'Login successful'})
    else:
        return Response({'message': 'Incorrect login credentials, please try again'})
    
@api_view(["POST"])
def register(request):
    print(request.data)
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    email = request.data["email"]
    password = request.data["password"]

    if None not in [first_name, last_name, email, password]:
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)  # if there is error in this like email exists, 2nd return occurs
        new_user.save()
        # TBD: login in the new user
        return Response({"message":"Registration successful"})
        
    return Response({"message":"Registration unsuccesful"})
