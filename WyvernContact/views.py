from django.shortcuts import render
from .forms import ContactForm


# Create your views here.

def contact(request):
    cf = ContactForm()
    return render(request, "contact.html", {'formu': cf})
