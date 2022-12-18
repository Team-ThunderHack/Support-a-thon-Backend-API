from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import json
from ..models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create(request):
    received_json_data=json.loads(request.body)
    key = received_json_data['key']
    name = received_json_data['name']
    email = received_json_data["email"]
    password = received_json_data["password"]
    if(key=='73627'):
        user = Users(name=name,email=email,password=password)
        user.save()
        return Response("User Created Successfully")
    else:
        return Response("Invalid Key")