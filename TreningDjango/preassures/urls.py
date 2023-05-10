from django.urls import path
from . import views

app_name = 'preassures'

urlpatterns = [
    path('', views.intro, name='intro'), # 127.0.0.1:8000/preasssures/
    path('list/', views.PreassureList.as_view(), name='list'),
    path('create/', views.PreassureCreate.as_view(), name='create'),
    path('display/<int:pk>/', views.PreassureDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.PreassureUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.PreassureDelete.as_view(), name='delete')
]