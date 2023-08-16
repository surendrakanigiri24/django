from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Buliding dictionary for dynamic content
months = {
    "January": "I am the january",
    "February": "I am the feb",
    "march": "I am the march",
    "april": "I am the april",
    "may": "I am the may",
    "june": "I am the june",
    "july": "I am the july",
    "august": "I am the august",
    "september": "I am the september",
    "october": "I am the october",
    "november": "I am the november",
    "december": "I am the december"
}

# Create your views here.

def index (request):
    return HttpResponse("I am working!")

def february (request):
    return HttpResponse("I'm february")

def march (request):
    return HttpResponse("I'm march")

# Dynamic code building

def monthly_challenge_using_numbers (request, month):
    # Redirection
    months_keys = list(months.keys())

    if(month > len(months_keys)):
        return HttpResponseNotFound("Invalid month !")

    redirect_month = months_keys[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

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

# Even more advanced code building

def monthly_challenge_dynamic_appending (request, month):
    try:
        challege_text = months[month]
        print(challege_text)
        return HttpResponse(challege_text)
    except:
        return HttpResponseNotFound("Not a valid month !")
    