#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to my Portfolio!</h1>") 

def v1(response):
    return HttpResponse("<h1>view </1>")
