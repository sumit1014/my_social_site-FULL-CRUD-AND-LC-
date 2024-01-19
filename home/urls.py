from django.contrib import admin
from django.urls import path, include
from home import views
app_name = 'home'
urlpatterns = [
    path('', views.home_page, name="home"),
    path('contact', views.contact_page, name="contact_page"),
    path('about', views.about_page, name="about"),
    path('signup', views.handlesignup, name="signup_page"),
    path('login', views.handlelogin, name="login_page"),
    path('logout', views.handleLogout, name="handleLogout"),
    path('profile_page', views.profile_page, name="profile_page"),
    path('edit_profile', views.edit_profile, name="edit_profile"),   
]