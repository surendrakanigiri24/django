from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index (request):
    return HttpResponse("I am working!")

def february (request):
    return HttpResponse("I'm february")

def march (request):
    return HttpResponse("I'm march")

def monthly_challenge (request, month):
    challenge_text = None

    if month == "January":
        challenge_text = "I am January"
    elif month == "February":
        challenge_text = "I am February"
    elif month == "march":
        challenge_text = "I am march"
    else:
        return HttpResponseNotFound("Not a valid month !")

    return HttpResponse(challenge_text)