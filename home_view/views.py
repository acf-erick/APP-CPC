from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PessoaFisica

class HomeView(TemplateView):
    template_name = 'home_view/home.html'

