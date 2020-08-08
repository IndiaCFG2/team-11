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
