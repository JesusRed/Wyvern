from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage


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
            email = EmailMessage("New contact from Wyvern! {}".format(subject),
                                 "El siguiente usuario {} con el correo {} dice:\n\n {}".format(name, email, message),
                                 "",
                                 ["villalf19@gmail.com"],
                                 reply_to=[email])

            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?invalid")
    return render(request, "contact.html", {'formu': cf})
