from django.shortcuts import render, HttpResponse
from WyvernAdmin.models import Poster


# Create your views here.

def home(request):
    return render(request, "home.html")


def posters(request):
    posters = Poster.objects.all()
    return render(request, "posters.html", {"posters": posters})


def critics(request):
    return render(request, "critics.html")


def forum(request):
    return render(request, "forum.html")


def contact(request):
    return render(request, "contact.html")
