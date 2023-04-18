from django.urls import path
from . import views

# Każda aplikacja (tj. main) powinna mieć własny plik urls.py

urlpatterns = [
    path('', views.hello) # Uruchamiamy widok hello, gdy użytkownik niczego nie wpisze po 127.0.0.1:8000/
]