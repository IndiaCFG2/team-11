from django.db import models
from Schools.models import Schools
from django.urls import reverse

# Create your models here.

class Subjects(models.Model):
	class Meta:
	    verbose_name_plural = 'Subjects'
	name = models.CharField(max_length=100)
	url = models.URLField(max_length=100)

	def __str__(self):
	    return self.name


class Teachers(models.Model):
	class Meta:
	    verbose_name_plural = 'Teachers'
	REGISTER = (
	    ('Registered', 'Registered'),
	    ('Not Registered', 'Not Registered'),
	)
	TEST = (
	    ('Taken', 'Taken'),
	    ('Not Taken', 'Not Taken'),
	)
	college = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	status = models.CharField(max_length=100, choices=REGISTER, default='Not Registered')
	subjects = models.CharField(max_length=1000)
	test_1 = models.CharField(max_length=100, choices=TEST, default='Not Taken')
	test_2 = models.CharField(max_length=100, choices=TEST, default='Not Taken')
	test_3 = models.CharField(max_length=100, choices=TEST, default='Not Taken')
	test_4 = models.CharField(max_length=100, choices=TEST, default='Not Taken')
	progress_test = models.IntegerField()
	progress_tutorial = models.IntegerField()

	def __str__(self):
	    return self.name


class Stats(models.Model):
	class Meta:
	    verbose_name_plural = 'Stats'
	TUTORIALS = (
	    ('Watched', 'Watched'),
	    ('Not Watched', 'Not Watched'),
	)
	teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
	tutorials = models.CharField(max_length=100, choices=TUTORIALS, default='Not Watched')
	subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

	def __str__(self):
	    return self.teacher.name


class Query(models.Model):
	class Meta:
	    verbose_name_plural = 'Queries'
	    
	teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length = 1000, help_text="Please don't exceed 450 characters.")

	def __str__(self):
	    return self.teacher.name

	def get_absolute_url(self):
	    return reverse('query-detail', kwargs={'pk': self.pk})

