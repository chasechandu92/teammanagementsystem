from django.db import models
from django_mysql.models import EnumField

class Member(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20)
	email = models.EmailField()
	role = EnumField(choices=['admin', 'regular'])

	def __str__(self):
		return self.first_name+', '+self.email
