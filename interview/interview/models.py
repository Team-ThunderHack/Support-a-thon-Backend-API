from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Analysis(models.Model):
    email = models.CharField(max_length=200,null=True)
    questionID = models.IntegerField(null=True)
    wpm = models.IntegerField(null=True)
    fillerWords = models.CharField(max_length=500,null=True)
    fillerPhrases = models.CharField(max_length=500,null=True)
    recommendation = models.CharField(max_length=2000,null=True)