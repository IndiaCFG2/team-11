from django.contrib import admin
from .models import Subjects
from .models import Teachers
from .models import Stats

# Register your models here.
myModels = [Subjects, Teachers, Stats]  # iterable list
admin.site.register(myModels)
