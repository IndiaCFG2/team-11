from django.contrib import admin
from . models import Employee
from . models import Users


<<<<<<< HEAD
# Register your models here.
myModels = [Employee, Users]  # iterable list
admin.site.register(myModels)
=======
admin.site.register(models.Employee)
admin.site.register(models.Manager)
admin.site.register(models.Assign)
>>>>>>> e2ce7e57c332544b9ecd95e7e8f6e1d40153feb8
