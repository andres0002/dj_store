# py
# django
from django.urls import path
# third
# own
from apps.store.views import store, category

urlpatterns = [
    path('', store, name='home'),
    path('category/<int:pk>/', category, name='category'),
]