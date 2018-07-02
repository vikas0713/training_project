"""
This file was created at Smartbuzz Inc.
For more information visit http://www.smartbuzzinc.com
"""
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):

	template_name = 'signin.html'
	extra_context = {"name":"hello", "username": "vikas"}


def index_view(request):
	return render(
		request,
		'signin.html',
		{"name": "hello", "username": "lata"}
	)