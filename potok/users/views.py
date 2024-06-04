from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from django.urls import reverse
from django.contrib.auth import logout


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect(reverse('users:login'))


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if type(user) in [type(Expert()), type(Doctor())]:
                messages.success(request, 'Вы успешно авторизовались')
                return redirect(reverse('threadPrediction:research'))
            else:
                messages.success(request, 'Вы успешно авторизовались!')
                return redirect('admin:index')
        else:
            messages.error(request, 'Неверно введён пароль или логин! Или такого пользователя не существует')

    form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})
