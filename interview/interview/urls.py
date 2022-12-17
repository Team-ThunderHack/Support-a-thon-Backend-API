from django.contrib import admin
from django.urls import path
from interview.views import create
from interview.views import authenticate
from interview.views import doAnalysis
from interview.views import getDetails
from interview.views import doTextAnalysis
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create",create.create),
    path("authenticate/",authenticate.authenticate),
    path("doAnalysis/",doAnalysis.doAnalysis),
    path("doTextAnalysis/",doTextAnalysis.doTextAnalysis),
    path("getDetails/",getDetails.getDetails),
]