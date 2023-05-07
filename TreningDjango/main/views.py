from django.shortcuts import HttpResponse, render
from django.views import View
from django.views.generic import TemplateView
import random

class CatTemplateView(TemplateView):
    template_name = 'main/cat.html'
    extra_context = {'name':'Blanunia'}


class CatView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Jestem kotem, miau...')


class HelloView(TemplateView):
    template_name = 'main/hello.html'
    # extra_context = {'lucky_number': random.randint(1, 32)}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lucky_number'] = random.randint(1, 32)
        return context



class AuthorView(TemplateView):
    template_name = 'main/author.html'


# 127.0.0.1:8000/1/2/3/
def params1(request, a, b, c):
    suma = a + b + c
    return HttpResponse(f'Parametry: {a=} {b=} {c=} {suma=}')

# 127.0.0.1:8000?a=1&b=2&c=3
def params2(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    c = request.GET.get('c', '')
    suma = int(a) + int(b) + int(c)
    #suma = sum(int(x) for x in (a, b, c))
    return HttpResponse(f'Parametry: {a=} {b=} {c=} {suma=}')

# Stwórz widok w aplikacji main, który wyświetli bmi obliczone dla takiego adresu: 127.0.0.1:8000/bmi?waga=108&wzrost=1.8
# BMI obliczamy dzieląc masę ciała w kg przez (wzrost w metrach) do kwadratu
def bmi(request):
    try:
        waga = int(request.GET.get('waga', 0))
        wzrost = float(request.GET.get('wzrost', '1.0'))
    except:
        return HttpResponse('Musisz podać wagę w kg i wzrost w metrach, np. /bmi?waga=108&wzrost=1.8')
    else:
        return HttpResponse(f'Twoje BMI wynosi {waga / wzrost ** 2:.2f}')
