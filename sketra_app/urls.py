from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # This maps the home page to the home view
     path('registerpg/', views.registerpg, name='registerpg'),
    path('', views.loginpg, name='loginpg'),
 
    path('houseplan/', views.houseplan, name='houseplan'),
     path('generation/', views.generation, name='generation'),
]
