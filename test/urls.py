from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('house/<int:house_id>', views.house, name = 'house'),
    path('<int:manush_id>/add_house', views.add_house, name = 'add_house'),
    path('<int:house_id>/update_house', views.update_house, name = 'update_house'),
    path('bookmark', views.bookmark, name = 'bookmark'),
    path('login', views.login_manush, name ='login'),
    path('logout', views.logout_manush, name ='logout'),
    path('registration', views.register_manush, name = 'registration'),
    path('update', views.update_profile, name = 'update_profile'),
    path('all_houses', views.all_house, name='all_houses'),
    path('add_bookmark/', views.add_bookmark, name = "add_bookmark"),
    path('manage_house', views.manage_houses, name = 'manage_houses'),
    path('findHome', views.findHome, name = 'findHome')
    
]

