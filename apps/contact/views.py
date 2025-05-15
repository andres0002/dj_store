# py
import logging
# django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
# third
# own
from apps.contact.forms import ContactForm
from apps.base.utils.emails import send_email_gmail_with_email_message

# Create your views here.

logger = logging.getLogger(__name__)

def contact(request, *args, **kwargs):
    template_name = 'contact.html'
    success_url = reverse_lazy('base:home')
    # print(request.path)
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            ok, error = send_email_gmail_with_email_message(
                subject=f'Contact User -> {name}',
                body={'template_name':'contact_email.html','name':name,'email':email,'content':content},
                to=['test-aap@yopmail.com'],
                reply_to=['test-aap@yopmail.com']
            )
            if ok:
                messages.success(request,'Mail send successfully.')
                logger.info(f'Mail send successfully -> Data -> Name: {name}, email: {email}, content: "{content}".')
                return redirect(success_url)
            else:
                messages.error(request,'Mail send errorfully.')
                logger.error(f'Mail send errorfully -> Data -> Name: {name}, email: {email}, content: "{content}", error: {error}.')
        return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})