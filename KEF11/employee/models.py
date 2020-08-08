from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('candidate-detail', kwargs={'pk': self.pk})
