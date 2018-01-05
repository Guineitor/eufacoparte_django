# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


#define upload path dinam...
def upload_localtion(instance, filename):
	return "%s_%s" %(instance.id, filename)


class PageLayout(models.Model):
	content = models.TextField()
	position = models.IntegerField()
	page = models.IntegerField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	image =  models.ImageField(upload_to=upload_localtion,
		null=True, 
		blank=True, 
		width_field="width_field",
		height_field="height_field")

	def __str__(self):
		return self.content