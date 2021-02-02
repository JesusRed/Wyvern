from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    name = forms.CharField(label="Name", required=True)
    subject = forms.CharField(label="Subject", widget=forms.Select)
    email = forms.CharField(label="Email", required=True)
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea)
