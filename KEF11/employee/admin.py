from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.Manager)
admin.site.register(models.Assign)
