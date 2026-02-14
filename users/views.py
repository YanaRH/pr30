from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Перенаправление на главную
        else:
            messages.error(request, 'Неверные учетные данные')
    return render(request, 'users/login.html')