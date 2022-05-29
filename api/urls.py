from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_item),
    path('add/', views.add_item),
    path('sign-in/', views.sign_in),
]