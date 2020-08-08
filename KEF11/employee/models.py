from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('candidate-detail', kwargs={'pk': self.pk})
class Users(models.Model):
    useremail=models.EmailField()
    is_super=models.BooleanField(default=False)


class Manager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    manager=models.ForeignKey(User, on_delete=models.CASCADE,default=None)


class Assign(models.Model):
    employee_name=models.CharField(max_length=100)
    school_name=models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
