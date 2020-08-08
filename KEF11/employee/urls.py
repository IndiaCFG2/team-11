from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_school,name='register_school' ),
    path('home/',views.home,name='home'),
]
