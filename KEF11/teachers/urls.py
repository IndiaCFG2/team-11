from django.urls import path
from . import views
from .views import (
    QueryCreateView,
    QueryUpdateView,
    QueryDeleteView,
    QueryDetailView
    )


urlpatterns = [
    path('', views.teacher, name='teacher-home'),
    path('queries/<int:pk>/', QueryDetailView.as_view(), name='query-detail'),
    path('queries/<int:pk>/update/', QueryUpdateView.as_view(), name='query-update'),
    path('queries/<int:pk>/delete/', QueryDeleteView.as_view(), name='query-delete'),
    path('queries/new/', QueryCreateView.as_view(), name='query-create'),
    path('tutorials/', views.tutorial, name='tutorial-home'),
    path('tests/', views.test, name='test-home'),
    path('queries/', views.query, name='queries-home'),
    path('teacherlogin/', views.teacherlogin, name='teacher-teacherlogin'),
    path('about/', views.about, name='teacher-about'),
    path('teacher/',views.teacher,name='teacher-teacher'),
]