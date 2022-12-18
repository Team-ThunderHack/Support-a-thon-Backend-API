from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import json
from ..models import Analysis
from ..serializers import AnalysisDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import spacy
nlp = spacy.load('/Users/anilaswani/opt/anaconda3/lib/python3.9/site-packages/en_core_web_sm/en_core_web_sm-2.2.0')
from spacy import displacy

def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

@api_view(['POST'])
def doTextAnalysis(request):
    received_json_data=json.loads(request.body)
    key = received_json_data['key']
    print(key)
    questionID = received_json_data["questionID"]
    email = received_json_data["email"]
    s = received_json_data["text"]
    timeDuration = received_json_data["timeDuration"]
    fillerWordList = ["Well","um","uh","Hmm","Like","Actually","Basically","Seriously", "Right","mhm","uh","huh"]
    fillerPhraseList =  ["You see","You know","I mean","You know what I mean","At the end of the day","Believe me",
                        "I guess","I suppose","Or something","Okay so"]
    notMention = ['youtube','tiktok','instagram','moj']
    mention = ['LinkedIn','Github']
    if(key=='73627'):
        doc = nlp(s)
        entitiesInS = []
        for ent in doc.ents:
            # if(ent.label=='ORG'):
            entitiesInS.append(ent.text)

        wpm = (len(s.split(" "))*60)/int(timeDuration)
        fillerWordsInS = []
        fillerPhrasesInS = []
        notMentioninS = []
        mentionInS = []

        for word in fillerWordList:
            k = isSubstring(word.lower(),s.lower())
            if(k!=-1):
                fillerWordsInS.append(word)

        for word in notMention:
            k = isSubstring(word.lower(),s.lower())
            if(k!=-1):
                notMentioninS.append(word)

        for word in mention:
            k = isSubstring(word.lower(),s.lower())
            if(k==-1):
                mentionInS.append(word)
        s1=""
        s2=""
        if(len(notMentioninS)==0):
            s1=s1+""
        elif(len(notMentioninS)==1):
            s1=s1+"We would like to mention that it would be better if you avoid mentioning about "+notMentioninS[0]+" in your interview."
        else:
            s1=s1+"We would like to mention that it would be better if you avoid mentioning about "+notMentioninS[0]+" and "+notMentioninS[1]+" in your interview."

        if(len(mentionInS)==0):
            s2+=""
        elif(len(mentionInS)==1):
            s2=s2+"It would be further better if you could mention about your "+mentionInS[0]+" profile in the interview."
        else:
            s2=s2+"It would be further better if you could mention about your "+mentionInS[0]+" and "+mentionInS[1]+" profile in the interview."

        recommendationString = s1+s2

        for word in fillerPhraseList:
            k = isSubstring(word.lower(),s.lower())
            if(k!=-1):
                fillerPhrasesInS.append(word)
        analysisDone = Analysis(email=email,questionID=int(questionID),wpm=wpm,fillerWords=json.loads(json.dumps(fillerWordsInS)),fillerPhrases=json.loads(json.dumps(fillerPhrasesInS)),recommendation=recommendationString)
        analysisDone.save()
        resultData = Analysis.objects.filter(email=email,questionID=questionID)
        res = AnalysisDetails(resultData,many=True)
        return Response(res.data)

    else:

        return Response("Invalid Key")