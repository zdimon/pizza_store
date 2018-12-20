from django.shortcuts import render
from django.views.generic import TemplateView, DetailView   
from .models import Page

class InfoView(DetailView):
    model = Page