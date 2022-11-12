from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate


class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'],
                                     email=cd['email'],
                                     password=cd['password1'])

            messages.success(request, 'You registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    class_form = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('home:home')
            messages.error(request, 'Username or Password is WRONG', 'danger')
        return render(request, self.template_name, {'form': form})

