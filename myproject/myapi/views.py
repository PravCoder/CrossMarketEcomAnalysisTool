from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(["GET"])
def home(request):
    print(f"USER: {request.user}")
    for user in User.objects.all():
        print(user)
    return Response({"message":request.user.username})

@api_view(["POST"])
def login_view(request):
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
    email = request.data["email"]
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    password = request.data["password"]

    serializer = UserSerializer(data=request.data)
    print("!...FLAG1...!" + str(serializer.is_valid()))
    if serializer.is_valid():
        # Save user object
        print("!...FLAG2...!")
        user = serializer.save()
        print("!...FLAG3...!")
        # Authenticate user
        user = authenticate(request=request._request, username=user.email, password=request.data['password'])
        print("!...FLAG4...!"+str(user))
        if user:
            print("!...FLAG5...!")
            login(request._request, user)
            print("!...FLAG1...!")
            return Response({"message": "Registration successful and user logged in."}, status=status.HTTP_201_CREATED)
        else:
            # Authentication failed, return error response
            return Response({"message": "Unable to log in user."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Invalid serializer data, return error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

