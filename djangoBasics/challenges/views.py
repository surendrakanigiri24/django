from django.shortcuts import render
from django.urls import reverse # allows retrieving url details from the url's.py file through the name value provided.
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
    list_items = ""
    months_keys = list(months.keys())

    for month in months_keys:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response = f"<ul>{list_items}</ul>"
    return HttpResponse(response)


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
    redirect_path = reverse("monthly-challenge", args=[redirect_month]) # Because of this we can avoid hardcoded path like /challenges
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)

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
        resopnse = f"<h1>{challege_text}</h1>"  # Html tag appending
        return HttpResponse(resopnse)
    except:
        return HttpResponseNotFound("<h1>Not a valid month!</h1>")
    