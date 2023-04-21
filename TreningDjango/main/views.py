from django.shortcuts import HttpResponse

# Widok to funkcja, która przyjmuje HttpRequest i zwraca HttpResponse

def hello(request):
    return HttpResponse('Hello world!')

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
