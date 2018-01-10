# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from enum import Enum
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
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
	template_name = "sobre.html"
	context = {
		"model": "model" 
	}
	return render(request=request, template_name=template_name, context=context)



def load_eventos(request, id=2):
	template_name  = "eventos.html"
	queryset_list = EventPicture.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(id__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list.order_by('id'), 1)
	page_request_var = "page"
	page = request.GET.get(page_request_var)

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(id)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	
	context = {
		"object_list": queryset, 
		"page_request_var": page_request_var
	}
	return render(request=request, template_name=template_name, context=context)


#get pagination from pictures 
def load_eventPicture(request, id=1):
	url_ajax = '/ajax/eventos/'
	data = {
		'next_url' : 'teste',
		'previouos_url': 'teste', 
		'url_ajax': url_ajax
	}

	return JsonResponse(data)



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

		 