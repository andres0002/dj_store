# py
# django
from django.urls import path
# third
# own
from apps.orders.views import process_order

urlpatterns = [
    path('process_order/', process_order, name='process_order'),
]