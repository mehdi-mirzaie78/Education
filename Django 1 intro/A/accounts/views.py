from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'You registered successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is WRONG', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You logged out successfully', 'success')
    return redirect('home')


@login_required
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information updated successfully', 'success')
            return redirect('home')
    else:
        form = UserProfileForm(instance=current_user)
    return render(request, 'profile.html', {'form': form})
