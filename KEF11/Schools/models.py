from django.db import models
from django.utils import timezone
import datetime
from employee.models import Employee

# Create your models here.

class Schools(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.IntegerField()
	headmaster = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
