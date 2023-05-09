from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('list/', views.NewsList.as_view(), name='list'),
    path('detail/<int:id>/', views.news_detail, name='detail') # 127.0.0.1:8000/news/detail/1/
]