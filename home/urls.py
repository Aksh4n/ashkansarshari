from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('contact', views.contact , name="contact"),
    path('fa', views.fa , name="fa"),
    path('order', views.order , name="order"),





]
