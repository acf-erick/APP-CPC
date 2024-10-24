from django.db import models


class PessoaJuridica(models.Model):
    name = models.CharField(verbose_name="Nome Completo", max_length=255, null=False, blank=False)
    cpf = models.IntegerField(verbose_name="CPF", max_length=15, null=False, blank=False)
    email = models.EmailField(verbose_name="E-mail", max_length=255, null=False, blank=False)
    phone = models.CharField(verbose_name="Telefone", max_length=16, null=False, blank=False)
    birth_date = models.DateField(verbose_name="Data de Nascimento", null=False, blank=False)
    cep = models.IntegerField(verbose_name="CEP", null=False, blank=False)
    password = models.CharField(verbose_name="Senha", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)