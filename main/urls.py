from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('launches/', views.launches, name='launches'),
    path('history/', views.history, name='history'),
    path('starlink/', views.starlink, name='starlink'),
    path('rockets/', views.rockets, name='rockets'),
    path('roadster/', views.roadster, name='roadster'),
    path('extra/', views.extra, name='extra'),
]