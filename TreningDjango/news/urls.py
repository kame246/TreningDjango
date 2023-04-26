from django.urls import path
from .views import post_list

app_name = 'news'

urlpatterns = [
    path('list/', post_list, name='list'),
]