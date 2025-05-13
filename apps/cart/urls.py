# py
# django
from django.urls import path
# third
# own
from apps.cart.views import cart, add_product, add_product_in_cart, delete_product, subtract_product, clean_cart

urlpatterns = [
    path('', cart, name='home'),
    path('add_product/<int:pk>/', add_product, name='add_product'),
    path('add_product_in_cart/<int:pk>/', add_product_in_cart, name='add_product_in_cart'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('subtract_product/<int:pk>/', subtract_product, name='subtract_product'),
    path('clean_cart/', clean_cart, name='clean_cart'),
]