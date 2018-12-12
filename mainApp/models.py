from django.db import models
from django import forms

class Employee(models.Model):
	name = models.CharField(max_length=30)
	position = models.CharField(max_length=30)
	date_employment = models.DateField()
	wage = models.IntegerField()

	def __str__(self):
		return self.name
