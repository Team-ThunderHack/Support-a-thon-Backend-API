from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from ..models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create(request):
    key = request.query_params.get("key")
    name = request.query_params.get("name")
    email = request.query_params.get("email")
    password = request.query_params.get("password")
    if(key=='73627'):
        user = Users(name=name,email=email,password=password)
        user.save()
        return Response("User Created Successfully")
    else:
        return Response("Invalid Key")