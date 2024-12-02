from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PessoaFisica

class HomeView(TemplateView):
    template_name = 'home_view/home.html'

class UserTypeView(TemplateView):
    template_name = 'home_view/userType.html'


class PjSignUpView(TemplateView):
    template_name = 'home_view/pjSignUp.html'

class PfSignUpView(TemplateView):
    template_name = 'home_view/pfSignUp.html'

def create_pessoa_fisica(request):
        if request.method == 'POST':
            PessoaFisica.objects.create(
                name=request.POST['name'],
                rg=request.POST['rg'],
                cpf=request.POST['cpf'],
                birth_date=request.POST['birth_date'],
                cep=request.POST['cep'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                password=request.POST['password'],
        )
        
        return render(request, 'home_view/pfSignUp.html')

def delete_pessoa_fisica(request, id):
        pessoa = get_object_or_404(PessoaFisica, id=id)
        pessoa.delete()
        
def update_pessoa_fisica(request, id):
        pessoa = get_object_or_404(PessoaFisica, id=id)
        if request.method == 'POST':
            pessoa.name = request.POST['name']
            pessoa.phone = request.POST['phone']
            pessoa.email = request.POST['email']
            pessoa.save()
            
        return render(request, 'home_view/pfSignUp.html', {'pessoa': pessoa})
