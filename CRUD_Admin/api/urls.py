# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.food_list, name='food_list'),
    path('foods/add/', views.food_create, name='food_create'),
    path('foods/<int:pk>/edit/', views.food_update, name='food_update'),
    path('foods/<int:pk>/delete/', views.food_delete, name='food_delete'),
]