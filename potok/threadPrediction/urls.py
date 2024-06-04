from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'threadPrediction'

urlpatterns = [
    path('researchs/', researchsShowView, name='research'),
    path('researchs/upload/', addResearch, name='upload'),
    path('showResearch/', showResearch, name='showResearch'),
    path('users/', include('users.urls')),
]


