# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Response(models.Model):
	name=models.CharField(max_length=100)
	roll_no=models.CharField(max_length=50)
	q1=models.CharField(max_length=500)
	q2=models.CharField(max_length=500)
	q3=models.CharField(max_length=500)
	q4=models.CharField(max_length=500)
	q5=models.CharField(max_length=500)

	def __str__(self):
		return self.name +' - ' + self.roll_no

	#def get_absolute_url(self):
	#	return reverse('form_view',kwargs={'pk': self.pk})


	
