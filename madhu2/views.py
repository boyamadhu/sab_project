from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def SQL(request):
    return HttpResponse('<h1 style="background-color:green">creating a table</h1>')