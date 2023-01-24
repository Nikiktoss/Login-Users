from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrateForm


def index(request):
    return render(request, 'main.html')


def logout_from_app(request):
    logout(request)
    return redirect('login_page')


def registrate_user(request):
    if request.method == "POST":
        form = UserRegistrateForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password2'])
            new_user.save()
            messages.success(request, 'Авторизация прошла успешно.')
            return redirect('main_page')
    else:
        form = UserRegistrateForm()
        return render(request, 'registration_page.html', context={'form': form})


def sign_in_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Авторизация прошла успешно.')
            return redirect('main_page')
        else:
            return redirect('login_page')
    else:
        return render(request, 'sign_in_page.html')
