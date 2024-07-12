from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('shop/', views.shop, name="shop"),
    path('detailProduct/<slug>', views.detailProduct, name="detailProduct"),
]