from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from .serializers import HomepageSerializer
from .models import TestModel


def HomepageView(ViewSet):
    return HttpResponse("Hello world")

    
    