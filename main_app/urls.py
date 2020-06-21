from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('applications/', views.applications_index, name='applications_index'),
    path('accounts/login/', 'django.contrib.auth.views.login', name='login'),
    # path('accounts/logout/', 'django.contrib.auth.views.logout', name='logout'),
]