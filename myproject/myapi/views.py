from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home(request):
    print("get request as been sent!!!!")
    return Response({"message":"This is some message"})


