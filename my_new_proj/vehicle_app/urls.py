from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('create/', views.vehicle_create, name='vehicle_create'),
    path('<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('<int:pk>/update/', views.vehicle_update, name='vehicle_update'),
    path('<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
]
