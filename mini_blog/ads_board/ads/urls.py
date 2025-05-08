from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_ad, name='add_ad'),
    path('edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),  # Путь для подробного просмотра
    path('signup/', views.signup, name='signup'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('', views.home, name='home'),  # Главная страница
]
