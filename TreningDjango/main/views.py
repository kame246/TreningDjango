from django.shortcuts import HttpResponse

# Widok to funkcja, która przyjmuje HttpRequest i zwraca HttpResponse

def hello(request):
    return HttpResponse('Hello world!')