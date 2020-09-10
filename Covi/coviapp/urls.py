from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('bot/', views.bot, name="bot"),
    path('chat_input/', views.chat_input, name="chat_input"),
    path('map/', views.map, name="map")

]
