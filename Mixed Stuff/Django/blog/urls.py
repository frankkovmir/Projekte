from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='landing-page'),
    path('home/', views.discrepancies, name ='blog-home'),
]
