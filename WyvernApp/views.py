from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "home.html")


def critics(request):
    return render(request, "critics.html")


def forum(request):
    return render(request, "forum.html")


def contact(request):
    return render(request, "contact.html")
