from django.urls import path , include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/' , views.loginPage, name= "login"),
    path('register/', views.register, name="register"),
    path('confirmation/', views.confirmationauthors, name='confirmation'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]