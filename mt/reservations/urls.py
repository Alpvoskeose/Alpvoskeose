from django.urls import path
from .views import reservation_list, reservation_create, reservation_edit, reservation_delete, status_list

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('create/', reservation_create, name='reservation_create'),
    path('<int:pk>/edit/', reservation_edit, name='reservation_edit'),
    path('<int:pk>/delete/', reservation_delete, name='reservation_delete'),
    path('statuses/', status_list, name='status_list'),
]
