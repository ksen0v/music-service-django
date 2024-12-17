from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from core import settings

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm

def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request, template_name='404.html', status=404)

def home(request):
    data = {'default_photo': settings.DEFAULT_USER_IMAGE}
    return render(request, "main_page.html", context=data)

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile_page.html'
    extra_context = {
        'default_photo': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

def logout_view(request):
    logout(request)
    return redirect('/')