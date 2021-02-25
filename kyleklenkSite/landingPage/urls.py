from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingPage, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('getStocks/', views.getStocks, name="getStocks"),
    path('buyStock/', views.buyStock, name="buyStock"),
]
