from django.db import models
from .models import PessoaFisica

class PessoaFisica(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome Completo", null=False, blank=False)
    rg = models.CharField(max_length=15, verbose_name="RG", null=False, blank=False)
    cpf = models.CharField(max_length=11, verbose_name="CPF", null=False, blank=False)
    birth_date = models.DateField(verbose_name="Data de Nascimento", null=False, blank=False)
    cep = models.IntegerField(verbose_name="CEP", null=False, blank=False)
    phone = models.CharField(max_length=16, verbose_name="Celular", null=False, blank=False)
    email = models.EmailField(verbose_name="E-mail", max_length=255, null=False, blank=False)
    password = models.CharField(verbose_name="Senha", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)



class PessoaJuridica(PessoaFisica):  # Herda de PessoaFisica
    company_name = models.CharField(max_length=255, verbose_name="Nome da Empresa", null=False, blank=False)
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ", null=False, blank=False)
  

#Início do CRUD da pessoa física
#Criar pessoa física

def create_pessoa_fisica(nome, rg, cpf, data_nascimento, celular, email):
    pessoa = PessoaFisica.objects.create(
        nome=nome,
        rg=rg,
        cpf=cpf,
        data_nascimento=data_nascimento,
        celular=celular,
        email=email
    )
    print(f"Adicionado: {pessoa}")


#Ler pessoas físicas

def read_all_pessoas_fisicas():
    pessoas = PessoaFisica.objects.all()
    for pessoa in pessoas:
        print(pessoa)

#Atualizar pessoa física

def update_pessoa_fisica(id, nome=None, rg=None, cpf=None, data_nascimento=None, celular=None, email=None):
    if PessoaFisica.objects.filter(id=id).exists():
        pessoa = PessoaFisica.objects.get(id=id)
        
        if nome is not None:
            pessoa.name = nome
        if rg is not None:
            pessoa.rg = rg
        if cpf is not None:
            pessoa.cpf = cpf
        if data_nascimento is not None:
            pessoa.birth_date = data_nascimento
        if celular is not None:
            pessoa.phone = celular
        if email is not None:
            pessoa.email = email
        
        pessoa.save()
        print(f"Atualizado: {pessoa}")
    else:
        print("Pessoa não encontrada.")

#Deletar pessoa física

def delete_pessoa_fisica(id):
    if PessoaFisica.objects.filter(id=id).exists():
        PessoaFisica.objects.filter(id=id).delete()
        print(f"Pessoa com ID {id} foi excluída.")
    else:
        print("Pessoa não encontrada.")
        
#Na prática

# Criar pessoas físicas
create_pessoa_fisica("Erick Anderson", "14.785.66-7", "", "2000-04-12", "(61) 981547567", "erick@gmail.com")
create_pessoa_fisica("Rafael Oliveira", "15.147.432-1", "1999-08-08", "(61) 91234-5678", "rafaelsantistagmail.com")

# Ler todas as pessoas físicas
print("\nLista de todas as pessoas físicas:")
read_all_pessoas_fisicas()

# Atualizar uma pessoa física
print("\nAtualizando a pessoa com ID 1:")
update_pessoa_fisica(1, nome="Erick Anderson", celular="(11) 98756-1987")

# Ler todas as pessoas físicas novamente após a atualização da pessoa com ID:1
print("\nLista de todas as pessoas físicas após atualização:")
read_all_pessoas_fisicas()

# Deletar uma pessoa física
print("\nDeletando a pessoa com ID 2:")
delete_pessoa_fisica(2)

# Ler todas as pessoas físicas após deletar a pessoa do ID:2
print("\nLista final de todas as pessoas físicas:")
read_all_pessoas_fisicas()
