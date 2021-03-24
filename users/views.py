from django.shortcuts import render, redirect
from . import forms
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def mascotasListado(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'mascotas/listado.html', {})

def PerfilUsuario(request):
    return render(request, 'registration/profile.html', {})

def salir(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')