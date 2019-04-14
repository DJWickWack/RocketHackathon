from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='index.html'),
    path('add/', views.trashtagAdd, name='addTag'),
]
