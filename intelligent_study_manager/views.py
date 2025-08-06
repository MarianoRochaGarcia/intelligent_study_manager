from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, ProfileImageForm

def login_view(request):

    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def register_view(request):
    if request.method == "GET":
        user_form = UserForm()
        form_image_profile = ProfileImageForm()
        context = {
            'user_form': user_form,
            'form_image_profile': form_image_profile
        }
        return render(request, 'register.html', context)
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('login_view')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
            form_image_profile = ProfileImageForm()
            context = {
                'user_form': form,
                'form_image_profile': form_image_profile
            }
            return render(request, 'register.html', context)
