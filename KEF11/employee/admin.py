from django.contrib import admin
from . models import Employee
from . models import Users


# Register your models here.
myModels = [Employee, Users]  # iterable list
admin.site.register(myModels)
