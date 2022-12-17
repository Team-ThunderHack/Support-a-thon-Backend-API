from django.contrib import admin
from django.urls import path
from interview.views import create
from interview.views import authenticate
from interview.views import doAnalysis
from interview.views import getDetails
from interview.views import doTextAnalysis
from rest_framework import permissions

urlpatterns = [
    path("api/admin", admin.site.urls),
    path("api/create",create.create),
    path("api/authenticate",authenticate.authenticate),
    path("api/doAnalysis",doAnalysis.doAnalysis),
    path("api/doTextAnalysis",doTextAnalysis.doTextAnalysis),
    path("api/getDetails",getDetails.getDetails),
]