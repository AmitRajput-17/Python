from django.contrib import admin
from django.urls import path
from yellowgame import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('singlegame/',views.singlegame,name='singlegame'),
    
]