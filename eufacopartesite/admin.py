# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import EventPicture, PageLayout




class EventPictureModelAdmin(admin.ModelAdmin):
	search_fields = ["image_labe"]
	class Meta:
		model = EventPicture
			


class PageLayoutModelAdmin(admin.ModelAdmin):
	search_fields = ["page"]
	class Meta:
		model = PageLayout

admin.site.register(EventPicture)
admin.site.register(PageLayout)
