from django.shortcuts import render
from WyvernCritics.models import Review


# Create your views here.
def critics(request):
    critics = Review.objects.all()
    return render(request, "critics.html", {"critics": critics})
