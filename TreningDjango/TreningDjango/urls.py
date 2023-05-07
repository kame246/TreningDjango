"""
URL configuration for TreningDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Tu podejmujemy decycje, do urls której aplikacji powinniśmy się udać
# Np. path('blog/', include('blog.urls')) powoduje przejście do urls.py aplikacji blog
# jeśli wpisano adres 127.0.0.1:8000/blog/<ewentualnie coś jeszcze>/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('survey/', include('survey.urls')),
    path('', include('main.urls')) # Załączamy plik urls.py z aplikacji main, gdy nie ma niczego po adresie 127.0.0.1:8000/
]
