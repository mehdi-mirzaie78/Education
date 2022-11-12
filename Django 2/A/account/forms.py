from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Your username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'sample@gmail.com'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Your password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'placeholder': 'Confirm your password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This username is already used')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email is already used')
        return email

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords must be the same')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
