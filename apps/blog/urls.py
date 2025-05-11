# py
# django
from django.urls import path
# third
# own
from apps.blog.views import blog, category, detail_post

urlpatterns = [
    path('', blog, name='home'),
    path('category/<int:pk>/', category, name='category'),
    path('<slug:slug>', detail_post, name='detail_post'),
]