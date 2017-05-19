# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Response

# Create your views here.
class form_view(CreateView):
	model = Response
	fields = ['name','roll_no','q1','q2','q3','q4','q5']