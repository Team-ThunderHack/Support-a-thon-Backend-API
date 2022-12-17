from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from ..models import Analysis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import AnalysisDetails
import json

@api_view(['POST'])
def getDetails(request):
    received_json_data=json.loads(request.body)
    key = received_json_data['key']
    email = received_json_data["email"]
    questionID = received_json_data["questionID"]
    if(key=='73627'):
        data = Analysis.objects.filter(email=email,questionID=questionID)
        res = AnalysisDetails(data,many=True)
        return Response(res.data)
    else:
        return Response("Invalid Key")
