from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm, success_url = '/'),name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),

    path('',frontGeneral, name='home'),
    path('juegos/',juegos,name='juegos'),
    path('noticias/',noticias,name='noticias'),
    path('perfil/',perfil,name='perfil'),
]
