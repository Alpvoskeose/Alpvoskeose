from django.urls import path
from .views import table_list, table_create, table_update, table_delete

urlpatterns = [
    path('', table_list, name='table_list'),
    path('create/', table_create, name='table_create'),
    path('<int:pk>/edit/', table_update, name='table_edit'),
    path('<int:pk>/delete/', table_delete, name='table_delete'),
]
