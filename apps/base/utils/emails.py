# py
# django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# third
from decouple import config
# own

def load_template_with_context(**kwargs):
    # Carga plantilla HTML con contexto
    html_content = render_to_string('contact_email.html', {
        'name': kwargs.get('name'),
        'email': kwargs.get('email'),
        'content': kwargs.get('content')
    })
    return html_content

def send_email_gmail_with_email_message(**kwargs):
    body = load_template_with_context(**kwargs.get('body'))
    email = EmailMultiAlternatives(
        from_email=config('EMAIL_HOST_USER_DEV'), # app, web.
        subject=kwargs.get('subject'),
        body=body,
        to=kwargs.get('to'),
        reply_to=kwargs.get('reply_to'),
    )
    try:
        # Adjuntar HTML como alternativa
        email.attach_alternative(body, "text/html")
        email.send()
        # ok...
        return (True,'Ningúno.')
    except Exception as error:
        # error...
        return (False,error)