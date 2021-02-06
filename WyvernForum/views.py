from django.shortcuts import render, HttpResponse


# Create your views here.

def forum(request):
    return render(request, "forum.html")

