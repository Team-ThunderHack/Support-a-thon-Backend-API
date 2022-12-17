from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from ..models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os

@api_view(['GET'])
def authenticate(request):
    email = request.GET.get("email")
    passwordRec = request.GET.get("password")
    key = request.GET.get("key")
    correctPassword = Users.objects.get(email=email)
    correctPassword=correctPassword.password
    if(key=='73627'):
        if(correctPassword==passwordRec):
            return Response("Correct Password")
        else:
            return Response("Incorrect Password")
    else:
        return Response("Invalid Key")