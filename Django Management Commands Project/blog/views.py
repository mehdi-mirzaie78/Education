from django.shortcuts import render
from django.http import HttpResponse
from .decorators import AuthenticationRequired


def home(request):
    print(request.META.get("HTTP_TOKEN"))
    return HttpResponse('Home is here')


def set_header(request):
    response = HttpResponse("HEADER SET")
    response['HTTP_TOKEN'] = "valid_token"
    return response


@AuthenticationRequired
def show(request):
    return HttpResponse("Hello World")
