from django.urls import path
from . import views


urlpatterns = [
    path('', views.teacher, name='teacher-home'),
    path('tutorials/', views.tutorial, name='tutorial-home'),
    path('tests/', views.test, name='test-home'),
    path('queries/', views.query, name='queries-home'),
]