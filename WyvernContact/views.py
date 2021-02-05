from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.

def contact(request):
    cf = ContactForm()
    if request.method == "POST":
        cf = ContactForm(data=request.POST)
        if cf.is_valid():
            name = request.POST.get("name")
            subject = request.POST.get("subject")
            email = request.POST.get("email")
            message = request.POST.get("message")

            return redirect("/contact/?valid")
    return render(request, "contact.html", {'formu': cf})
