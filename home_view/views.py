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

class LoginView(TemplateView):
    template_name = 'home_view/login.html'