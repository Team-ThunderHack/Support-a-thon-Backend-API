from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from ..models import Users
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os

@api_view(['POST'])
def authenticate(request):
    received_json_data=json.loads(request.body)
    email = received_json_data['email']
    passwordRec = received_json_data['password']
    key = received_json_data['key']
    correctPassword = (Users.objects.get(email=email))
    correctPassword=correctPassword.password
    if(key=='73627'):
        if(correctPassword==passwordRec):
            return Response("Correct Password")
        else:
            return Response("Incorrect Password")
    else:
        return Response("Invalid Key")