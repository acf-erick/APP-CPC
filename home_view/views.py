from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home_view/home.html'

class UserTypeView(TemplateView):
    template_name = 'home_view/userType.html'

class PfSignUpView(TemplateView):
    template_name = 'home_view/pfSignUp.html'


class PjSignUpView(TemplateView):
    template_name = 'home_view/pjSignUp.html'

class FriedsListView(TemplateView):
    template_name = 'home_view/friendsList.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parceiros'] = [
            'Trilhando Caminhos Ecoturismo',
            'Promoções e Eventos - Trilhas e Viagens',
            'Mais Agai',
            'Jardim dos Beija-Flores',
            'Cervejas Capivara',
            'Nascer do Sol',
            'Queen of Peppers',
            'Botica Caliandra',
            'Queijaria Rancharia',
            'Chácara Bosque do Cerrado',
            'Território Comunicação',
            'Suzana Cardoso',
            'Ateliê Anjico',
            'Ecs Fisioterapia',
            'MEI',
            'Brasília com Maria',
            'Chácara BOAZ'
        ]
        return context

class LoginView(TemplateView):
    template_name = 'home_view/login.html'