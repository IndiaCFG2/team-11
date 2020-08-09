from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_school,name='register_school' ),
    path('',views.home,name='home'),
    path('map/',views.map,name='map'),
    path('list_school/',views.schools_list,name='list_schools'),
    path('replies/',views.reply,name='reply'),
      path('signup/',views.register_employee,name='employee-create'),
     path('login/',views.login_asview,name='login'),
     path('logout/',views.logout_asview,name='logout'),
     path('delete/<int:id1>',views.delete,name="delete"),
     
]
