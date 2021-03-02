from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class PrecioPageView(TemplateView):
    template_name = 'precio.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


# Create your views here.
