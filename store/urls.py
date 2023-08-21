from django.urls import path

from  django.contrib.auth import views as auth_views

from store.views import HomeView

urlpatterns = [
    path('/', HomeView.as_view() ,name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/index.html'), name='logout'),
]
