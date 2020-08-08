from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_school,name='register_school' ),
    path('home/',views.home,name='home'),
    path('map/',views.map,name='map'),
    path('list_schools/',views.list_schools,name='list_schools'),
    path('',views.login,name='login'),
]
