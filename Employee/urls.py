from django.contrib import admin
from django.urls import path
from Employee import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='deletedata'),
    path('edit/<int:id>/', views.edit, name='updatedata'),
]
