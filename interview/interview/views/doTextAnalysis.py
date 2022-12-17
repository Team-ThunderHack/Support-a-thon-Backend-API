from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import json
from ..models import Analysis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

@api_view(['GET'])
def doTextAnalysis(request):
    key = request.GET.get('key')
    questionID = request.GET.get("questionID")
    email = request.GET.get("email")
    s = request.GET.get("text")
    timeDuration = request.GET.get("timeDuration")
    fillerWordList = ["Well","um","uh","Hmm","Like","Actually","Basically","Seriously", "Right","mhm","uh","huh"]
    fillerPhraseList =  ["You see","You know","I mean","You know what I mean","At the end of the day","Believe me",
                        "I guess","I suppose","Or something","Okay so"]
    if(key=='73627'):

        wpm = (len(s.split(" "))*60)/int(timeDuration)
        fillerWordsInS = []
        fillerPhrasesInS = []

        for word in fillerWordList:
            k = isSubstring(word.lower(),s.lower())
            if(k!=-1):
                fillerWordsInS.append(word)

        for word in fillerPhraseList:
            k = isSubstring(word.lower(),s.lower())
            if(k!=-1):
                fillerPhrasesInS.append(word)
        analysisDone = Analysis(email=email,questionID=int(questionID),wpm=wpm,fillerWords=json.loads(json.dumps(fillerWordsInS)),fillerPhrases=json.loads(json.dumps(fillerPhrasesInS)))
        analysisDone.save()
        
        jsonRes = json.dumps([questionID,wpm,fillerWordsInS,fillerPhrasesInS])
        jsonRes = json.loads(jsonRes)

        return Response(jsonRes)

    else:

        return Response("Invalid Key")