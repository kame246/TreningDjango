from django.urls import path
from . import views

app_name='survey'

urlpatterns = [
    path('send/', views.send_survey, name='send_survey'),
]