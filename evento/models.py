# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    eventoPrincipal= models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    dataEHoraDeInicio = models.DateField()
    palavrasChave = models.CharField(max_length=100)
    logotipo = models.CharField(max_length=50)
    realizador = models.ForeignKey('Pessoa')
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=15)



class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	
class Autor(Pessoa):
	curriculo = models.CharField(max_length=200)
	artigos = models.ForeignKey('ArtigoCientifico')
class PessoaJuridica(Pessoa):
	cnpj = models.CharField(max_length=50)
	razaoSocial = models.CharField(max_length=200)

class PessoaFisica(Pessoa):
	cpf = models.CharField(max_length=11)

class EventoCientifico(models.Model):
	issn = models.CharField(max_length=200)
	

class ArtigoCientifico(models.Model):
	nome = models.CharField(max_length=200)
	autores = models.ForeignKey('Autor')
	evento = models.ForeignKey('EventoCientifico')
		
	