from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def jersey(request):
    return HttpResponse('jersey will touch your heart')

