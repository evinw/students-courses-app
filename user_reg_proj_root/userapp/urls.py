from . import views
from django.urls import path
# import views for login and logout features
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('', views.index_page, name='index_page'),
    path('about/', views.about_page, name='about_page'),
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),

]
