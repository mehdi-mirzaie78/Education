from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set/', views.set_header, name='set'),
    path('show/', views.show, name='show')
]