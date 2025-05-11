# py
# django
from django.urls import path
# thrid
# own
from apps.contact.views import contact

urlpatterns = [
    path('', contact, name='home'),
]