from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	firstName = models.CharField(max_length 30)
	lastName = Models.CharField(max_length 30)
	timestamp = models.DateTimeField()