# py
# django
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# third
# own
from apps.store.models import CategoriesProduct, Products

# Create your views here.

@login_required(login_url='user:login')
def store(request, *args, **kwargs):
    template_name = 'store.html'
    # print(request.path)
    search = request.GET.get('search')
    products = Products.objects.filter(condition=True,available=True)
    if search:
        products = products.filter(
            Q(name__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Obtener categorías únicas
    categories_set = set()
    for product in products:
        categories_set.add(product.category)
    # Convertir a lista para usar en el template
    categories = list(categories_set)
    # Paginator.
    paginator = Paginator(products, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    products = paginator.get_page(page)
    return render(request, template_name, {'products':products,'categories':categories})

@login_required(login_url='user:login')
def category(request, pk, *args, **kwargs):
    template_name = 'store_category.html'
    # print(request.path)
    search = request.GET.get('search')
    category = CategoriesProduct.objects.filter(pk=pk).first()
    if category:
        products = Products.objects.filter(condition=True,available=True,category=category)
    else:
        products = Products.objects.filter(condition=True,available=True)
    if search:
        products = products.filter(
            Q(name__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Obtener categorías únicas
    categories_set = set()
    for product in products:
            categories_set.add(product.category)
    # Convertir a lista para usar en el template
    categories = list(categories_set)
    # Paginator.
    paginator = Paginator(products, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    products = paginator.get_page(page)
    return render(request, template_name, {'products':products,'categories':categories})