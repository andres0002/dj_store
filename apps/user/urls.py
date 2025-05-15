# py
# django
from django.urls import path
# third
# own
from apps.user.views import UsersLoginView, UsersLogoutView, UsersRegisterView, UsersPasswordChangeView, UsersPerfilView

urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    path('register/', UsersRegisterView.as_view(), name='register'),
    path('password_change/', UsersPasswordChangeView.as_view(), name='password_change'),
    path('perfil/<int:pk>/', UsersPerfilView.as_view(), name='perfil'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
]