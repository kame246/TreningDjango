from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Preassure

def intro(request):
    return render(request, 'preassures/intro.html')

class PreassureList(ListView):
    model = Preassure

class PreassureDetail(DetailView):
    model = Preassure

class PreassureCreate(CreateView):
    model = Preassure
    fields = ('sys', 'dia')
    success_url = reverse_lazy('preassures:list')

class PreassureUpdate(UpdateView):
    model = Preassure
    fields = ('sys', 'dia')
    success_url = reverse_lazy('preassures:list')

class PreassureDelete(DeleteView):
    model = Preassure
    success_url = reverse_lazy('preassures:list')
