from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send an email notification
            send_mail(
                f'Message from {form.cleaned_data["name"]} ({form.cleaned_data["email"]})',
                form.cleaned_data["message"],
                form.cleaned_data["email"],
                ['henryukomah@gmail.com.com'], # Replace with your email address
            )
            
            
            messages.success(request, 'Message sent')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
