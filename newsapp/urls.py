from django.contrib import admin
from django.urls import path, include
from news_api import views  # Replace with your app name
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('search/', views.search_news, name='search_news'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
