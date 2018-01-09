# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.db import models

# Create your models here.


#define upload path dinam...
def upload_localtion(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    model = instance.__class__
    new_id = model.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)



class PageLayout(models.Model):
	content = models.TextField()
	position = models.IntegerField()
	page = models.IntegerField(null=False, blank=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	image =  models.ImageField(upload_to=upload_localtion,
		null=True, 
		blank=True, 
		width_field="width_field",
		height_field="height_field")
	width_field = models.IntegerField(default=None)
	height_field = models.IntegerField(default=None)

	def __str__(self):
		return self.content


	def __int__(self):
		return self.position

	def __int__(self):
		return self.page



class EventPicture(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_DEFAULT)
	image =  models.ImageField(upload_to=upload_localtion,
		null=True, 
		blank=True, 
		width_field="width_field",
		height_field="height_field")
	label_image = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	width_field = models.IntegerField(default=300)
	height_field = models.IntegerField(default=400)

	def __str__(self):
		return self.label_image

	def __str__(self):
		return self.url_next

	def __str__(self):
		return self.url_previuous
