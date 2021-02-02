from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(
        attrs={
            'class': 'input', 'type': 'text', 'placeholder': 'Text input'
        }
    ))

    CHOICES = (('Asesoria', 'Asesoria'), ('Ventas', 'Ventas'))
    subject = forms.ChoiceField(label="Subject", choices=CHOICES, widget=forms.Select())

    email = forms.CharField(label="Email", required=True, widget=forms.EmailInput(
        attrs={
            'class': 'input is-black', 'type': 'email', 'placeholder': 'user@mail.xx'
        }
    ))

    message = forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={
            'class': 'textarea', 'placeholder': 'Type your message', 'rows': '5'
        }
    ))
