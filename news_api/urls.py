from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_news, name='search_news'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
