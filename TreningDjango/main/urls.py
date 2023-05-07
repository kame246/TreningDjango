from django.urls import path
from . import views

# Każda aplikacja (tj. main) powinna mieć własny plik urls.py

app_name = 'main'

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'), # Uruchamiamy widok hello, gdy użytkownik niczego nie wpisze po 127.0.0.1:8000/
    path('cat/', views.CatView.as_view(), name='cat'),
    path('cat2/', views.CatTemplateView.as_view(), name='cat2'),
    # path('cat2/', TemplateView(template_name='main/cat.html').as_view(), name='cat2'),
    path('author/', views.AuthorView.as_view(), name='author'),
    path('params1/<int:a>/<int:b>/<int:c>/', views.params1), # 127.0.0.1:8000/params1/1/2/3/
    path('params2/', views.params2), # 127.0.0.1:8000/params2?a=1&b=2&c=3
    path('bmi/', views.bmi)
]