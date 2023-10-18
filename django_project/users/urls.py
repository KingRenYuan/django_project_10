from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]
