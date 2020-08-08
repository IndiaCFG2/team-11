from django.contrib import admin
from .models import Subjects
from .models import Teachers
from .models import Stats
from .models import Query

# Register your models here.
myModels = [Subjects, Teachers, Stats, Query]  # iterable list
admin.site.register(myModels)
