from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, UpdateView   
from .models import Page
from django.forms import ModelForm
from ckeditor.fields import  CKEditorWidget


class InfoView(DetailView):
    model = Page
    
class PageEditView(UpdateView):
    model = Page  
    fields = ['title', 'content']  