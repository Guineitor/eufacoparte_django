# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from enum import Enum
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import PageLayout, EventPicture

# Create your views here.


	

def load_home(request, id=1):
	# model = get_object_or_404(Comment, page=id)
	template_name  = "index.html"
	context = {
		"model": "model" 
	}
	return render(request=request, template_name=template_name, context=context)


def load_sobre(request, id = None):
	# model = get_object_or_404(Comment, page=id)
	template_name  = "sobre.html"
	context = {
		"model": "model" 
	}
	return render(request=request, template_name=template_name, context=context)



def load_eventos(request, id=1):
	template_name  = "eventos.html"
	if id != None:
		event = get_object_or_404(EventPicture, id=id)
		context = {
			"event": event 
		}		
	else:
		print("no url found")
		context = {
			"event": "empty" 
		}

	return render(request=request, template_name=template_name, context=context)



def load_contato(request, id = None):
	# model = get_object_or_404(Comment, page=id)
	template_name  = "contato.html"
	context = {
		"model": "model" 
	}
	return render(request=request, template_name=template_name, context=context)


def load_participe(request, id = None):
	# model = get_object_or_404(Comment, page=id)
	template_name  = "index.html"
	context = {
		"model": "model" 
	}
	return render(request=request, template_name=template_name, context=context)


	
class PageEnum(Enum):
	index = 0
	sobre = 1
	eventos = 2
	participe = 3
	contato = 4

		 