from django.urls import path
from . import views

from employee.models import Assign

urlpatterns = [

     path('requests/',views.requests,name='requests'),
     
]
