from django.urls import path
from . import views

urlpatterns = [
    #to call that function in home
    path('', views.home, name='home'),
    path('wait/', views.wait, name='wait'),
    path('login/', views.login, name='login'),
    path('privacy/', views.privacy, name='privacy'),
    path('register/', views.register, name='register'),

]
