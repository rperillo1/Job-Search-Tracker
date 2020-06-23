from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('applications/', views.applications_index, name='applications_index'),
    path('applications/create/', views.ApplicationCreate.as_view(), name='applications_create'),
    path('applications/<int:pk>/', views.ApplicationShow.as_view(), name='applications_show'),
    path('applications/<int:app_id>/interview/', views.interview_index, name='interview_index'),
    path('applications/<int:app_id>/interview/form/', views.interview_form, name='interview_form'),
    path('applications/<int:app_id>/interview/create/', views.interview_create, name='interview_create'),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application_delete'),
    path('applications/<int:application_pk>/interview/<int:pk>/', views.InterviewShow.as_view(), name='interview_detail'),
    path('applications/<int:application_pk>/interview/<int:pk>/delete/', views.InterviewDelete.as_view(), name='interview_delete'),
    
]
