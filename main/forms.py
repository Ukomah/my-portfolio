from django import forms
from .models import ContactFormEntry

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormEntry
        fields = ['name', 'email', 'subject', 'message']