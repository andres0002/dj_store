# py
# djnago
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib import messages
# third
# own
from apps.user.models import Users
from apps.user.forms import LoginForm, UsersForm, PasswordChangeForm
from apps.user.mixins import LoginRequiredMixin

# Create your views here.

class UsersLoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('base:home')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class UsersLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('base:home')

class UsersRegisterView(View):
    template_name = 'register.html'
    model = Users
    form_class = UsersForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if (form.is_valid()):
            new_user = self.model(
                username = form.cleaned_data['username'],
                name = form.cleaned_data['name'],
                lastname = form.cleaned_data['lastname'],
                email = form.cleaned_data['email']
            )
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request, 'Successfully User register.')
            return redirect('user:login')
        messages.error(request, 'Errorful User register.')
        return render(request, self.template_name, {'form':form})

class UsersPasswordChangeView(LoginRequiredMixin, View):
    template_name = 'password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('user:login')
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = Users.objects.filter(pk=request.user.pk).first()
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            logout(request)
            messages.success(request, 'Successfully change password.')
            return redirect(self.success_url)
        messages.error(request, 'Errorful change password.')
        return render(request, self.template_name, {'form': form})

class UsersPerfilView(LoginRequiredMixin, UpdateView):
    model = Users
    form_class = UsersForm
    template_name = 'perfil.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully User updation.')
            return redirect(request.META.get('HTTP_REFERER', reverse('user:perfil', kwargs={'pk': request.user.pk})))
        messages.error(request, 'Errorful User updation.')
        return render(request, self.template_name, {'form':form})