from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm,CustomAuthenticationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm  # Opcional, se quiser usar um form personalizado