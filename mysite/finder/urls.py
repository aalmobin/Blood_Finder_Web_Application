from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [

    path('', views.home, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.updateprofile, name='update-profile'),
    path('search_blood/', views.search, name='search_blood'),
    path('login/', LoginView.as_view(template_name='finder/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='finder/logout.html'), name='logout'),
]
