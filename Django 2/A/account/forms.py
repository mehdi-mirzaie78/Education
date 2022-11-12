from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mt-2', 'placeholder': 'sample@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Your password'}))
