# py
# django
from django.shortcuts import render
# third
# own
from apps.services.models import Services

# Create your views here.

def services(request, *args, **kwargs):
    template_name = 'services.html'
    # print(request.path)
    services = Services.objects.all()
    return render(request, template_name, {'services':services})