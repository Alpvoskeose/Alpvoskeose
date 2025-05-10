from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ad_list, name='ad_list'),
    path('ads/list/', views.ad_list, name='ad_list'),  # Страница списка всех объявлений
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('', views.welcome, name='welcome'),
    path('ads/', views.ad_list, name='ad_list'),  # Список объявлений
    path('ads/create/', views.ad_create, name='ad_create'),  # Создание объявления
    path('ads/edit/<int:pk>/', views.ad_edit, name='ad_edit'),  # Редактирование объявления
    path('ads/delete/<int:pk>/', views.ad_delete, name='ad_delete'),  # Удаление объявления
    path('', views.ad_list, name='ad_list'),  # Список объявлений
    path('create/', views.ad_create, name='ad_create'),  # Создание объявления
    path('edit/<int:pk>/', views.ad_edit, name='ad_edit'),  # Редактирование объявления
    path('delete/<int:pk>/', views.ad_delete, name='ad_delete'),  # Удаление объявления
    path('list/', views.ad_list, name='ad_list'),  # Страница списка всех объявлений
    path('logout/', views.logout_view, name='logout'),  # Путь для выхода
]
