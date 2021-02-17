from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [

    path('', views.home, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='finder/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='finder/logout.html'), name='logout'),
]
