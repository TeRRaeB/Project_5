from django.shortcuts import render,redirect, get_object_or_404
from .models import ContactMessage
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from products.models import Review
from django.core.mail import send_mail
from django.conf import settings
from allauth.account.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    
def index(request):

    reviews = Review.objects.select_related("user").order_by("-created_at")
    
    return render(request, 'home/index.html', {"reviews": reviews})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thank You for Contacting Us! \
                          We have received your message and will get back to you shortly.")
            return redirect('contact')
        else:            
            messages.error(request, "Contact form error! Try again.")
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser)
def admin_panel(request): 
    contact_us = ContactMessage.objects.all()

    if request.method == 'POST':
        contact_us = request.POST.get('message_id')
        if contact_us: 
            contact_us = ContactMessage.objects.get(id=contact_us)
            contact_us.delete() 
            return redirect('admin_panel')

    return render(request, 'home/admin_panel.html', {'contact_us': contact_us})

@user_passes_test(lambda user: user.is_superuser)
def delete_message(request, contact_id):
    contact = get_object_or_404(ContactMessage, id=contact_id)
    
    if request.method == 'POST':
        contact.delete()        
        messages.warning(request, 'Message deleted successfully!')

        return redirect('admin_panel')  
    else:
        messages.error(request, 'There was an error deleting the message.')
        return redirect('admin_panel')