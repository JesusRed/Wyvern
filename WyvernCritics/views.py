from django import template
from django.shortcuts import render
from WyvernCritics.models import Review, Person, Role, Movie


# Create your views here.
def critics(request):
    role = Role.objects.all()
    person = Person.objects.filter(role__tipo='Director')
    critics = Review.objects.all()
    return render(request, "critics.html", {"critics": critics, "person": person, "role": role})


def director(request, person_id):
    person = Person.objects.get(id=person_id)
    movie = Movie.objects.filter(person=person)
    return render(request, "movies.html", {"person": person, "movie": movie})
