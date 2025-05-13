# py
# django
from django.shortcuts import render
# third
# own

# Create your views here.

def home(request, *args, **kwargs):
    template_name = 'base_home.html'
    # print(request.path)
    return render(request, template_name)