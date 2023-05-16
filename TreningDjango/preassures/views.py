from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Preassure

# @login_required
@permission_required(perm='preassures.view_preassure', raise_exception=True)
def intro(request):
    return render(request, 'preassures/intro.html')

# class PreassureList(LoginRequiredMixin, ListView):
#     model = Preassure

class PreassureList(PermissionRequiredMixin, ListView):
    model = Preassure
    permission_required = 'preassures.view_preassure'

class PreassureDetail(PermissionRequiredMixin, DetailView):
    model = Preassure
    permission_required = 'preassures.view_preassure'

class PreassureCreate(PermissionRequiredMixin, CreateView):
    model = Preassure
    fields = ('sys', 'dia')
    success_url = reverse_lazy('preassures:list')
    permission_required = 'preassures.add_preassure'

class PreassureUpdate(PermissionRequiredMixin, UpdateView):
    model = Preassure
    fields = ('sys', 'dia')
    success_url = reverse_lazy('preassures:list')
    permission_required = 'preassures.change_preassure'

class PreassureDelete(PermissionRequiredMixin, DeleteView):
    model = Preassure
    success_url = reverse_lazy('preassures:list')
    permission_required = 'preassures.delete_preassure'
