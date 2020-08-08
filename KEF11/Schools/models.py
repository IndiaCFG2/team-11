from django.db import models
from django.utils import timezone
import datetime
from employee.models import Employee
from django.contrib.auth.models import User

# Create your models here.

class Schools(models.Model):
	employee = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.IntegerField()
	headmaster = models.CharField(max_length=100)
	location=models.CharField(max_length=100,blank=True)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
