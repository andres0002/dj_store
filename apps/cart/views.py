# py
# django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# third
# own
from apps.cart.cart import Cart
from apps.store.models import Products

# Create your views here.

@login_required(login_url='user:login')
def cart(request, *args, **kwargs):
    template_name = 'cart.html'
    return render(request, template_name)

@login_required(login_url='user:login')
def add_product(request, pk, *args, **kwargs):
    cart = Cart(request)
    product = Products.objects.get(pk=pk)
    cart.add(product)
    # print(request.META)
    # redirige a la page desde donde se hace el reqeust, y sino al store.
    return redirect(request.META.get('HTTP_REFERER', reverse('store:home')))

@login_required(login_url='user:login')
def add_product_in_cart(request, pk, *args, **kwargs):
    cart = Cart(request)
    product = Products.objects.get(pk=pk)
    cart.add(product)
    return redirect('cart:home')

@login_required(login_url='user:login')
def delete_product(request, pk, *args, **kwargs):
    cart = Cart(request)
    product = Products.objects.filter(pk=pk).first()
    cart.delete(product)
    return redirect('cart:home')

@login_required(login_url='user:login')
def subtract_product(request, pk, *args, **kwargs):
    cart = Cart(request)
    product = Products.objects.filter(pk=pk).first()
    cart.subtract(product)
    return redirect('cart:home')

@login_required(login_url='user:login')
def clean_cart(request, *args, **kwargs):
    cart = Cart(request)
    cart.clean()
    return redirect('cart:home')