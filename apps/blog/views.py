# py
# django
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# third
# own
from apps.blog.models import Categories, Posts

# Create your views here.

def blog(request, *args, **kwargs):
    template_name = 'blog.html'
    # print(request.path)
    search = request.GET.get('search')
    posts = Posts.objects.filter(condition=True)
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(content__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Obtener categorías únicas
    categories_set = set()
    for post in posts:
        for category in post.categories.all():
            categories_set.add(category)
    # Convertir a lista para usar en el template
    categories = list(categories_set)
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, template_name, {'posts':posts,'categories':categories})

def category(request, pk, *args, **kwargs):
    template_name = 'blog_category.html'
    # print(request.path)
    search = request.GET.get('search')
    category = Categories.objects.filter(pk=pk).first()
    if category:
        posts = Posts.objects.filter(condition=True,categories=category)
    else:
        posts = Posts.objects.filter(condition=True)
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(content__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Obtener categorías únicas
    categories_set = set()
    for post in posts:
        for category in post.categories.all():
            categories_set.add(category)
    # Convertir a lista para usar en el template
    categories = list(categories_set)
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, template_name, {'posts':posts,'categories':categories})

def detail_post(request, slug, *args, **kwargs):
    template_name = 'blog_post.html'
    # print(request.path)
    post = get_object_or_404(Posts, slug=slug)
    return render(request, template_name, {'post': post})