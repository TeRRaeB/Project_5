from django.shortcuts import render 
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})