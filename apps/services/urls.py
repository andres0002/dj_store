# py
# django
from django.urls import path
# third
# own
from apps.services.views import services

urlpatterns = [
    path('', services, name='home'),
]