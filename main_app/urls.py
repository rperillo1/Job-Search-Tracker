from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('applications/', views.applications_index, name='applications_index'),
    path('applications/create/', views.ApplicationCreate.as_view(), name='applications_create'),
    path('applications/<int:app_id>/interview/', views.interview_index, name='interview_index'),
    path('applications/<int:app_id>/interview/create/', views.interview_create, name='interview_create'),
]
