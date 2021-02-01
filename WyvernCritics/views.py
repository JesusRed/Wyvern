from django import template
from django.shortcuts import render
from WyvernCritics.models import Review, Person, Role


# Create your views here.
def critics(request):
    role = Role.objects.all()
    person = Person.objects.filter(role__tipo='Director')
    critics = Review.objects.all()
    return render(request, "critics.html", {"critics": critics, "person": person, "role": role})
