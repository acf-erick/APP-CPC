from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home_view/home.html'

class PjPfView(TemplateView):
    template_name = 'home_view/pjPf.html'