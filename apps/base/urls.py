#py
# django
from django.urls import path
# third
# own
from apps.base.views import home

urlpatterns = [
    path('', home, name='home'),
]