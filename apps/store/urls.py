# py
# django
from django.urls import path
# third
# own
from apps.store.views import store

urlpatterns = [
    path('', store, name='home'),
]