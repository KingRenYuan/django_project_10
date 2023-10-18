from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def log_in(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return redirect('posts')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST) # 创建一个 LoginForm 对象，其中包含用户在登录表单中输入的数据。

        if form.is_valid():
            username = form.cleaned_data['username'] # 获取用户在登录表单中输入的用户名。
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password) # 使用 authenticate() 函数验证用户名和密码。如果成功，则返回一个 User 对象。
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})



def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form': form})

