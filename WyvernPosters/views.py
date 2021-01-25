from django.shortcuts import render
from WyvernPosters.models import Poster


# Create your views here.

def posters(request):
    posters = Poster.objects.all()
    return render(request, "posters/posters.html", {"posters": posters})
