from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.myfun, name='index'),
    path('index1/', views.index, name='index1'),
    path('', views.index1, name='index2'),
    path('emp/', views.emp, name='emp'),
    #session
    path('ssession',views.setsession),
    path('gsession',views.getsession),
    # cookies
    path('scookie',views.setcookie),
    path('gcookie',views.getcookie)

]
