# core/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)
