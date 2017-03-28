# -*- coding: utf-8 -*-
from django.http import HttpResponse
from .models import Evento
from .models import Pessoa
from .models import PessoaFisica
from .models import PessoaJuridica
from .models import Autor
from .models import ArtigoCientifico


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/evetos'>Eventos</a></li>
                    <li><a href='/pessoas'>Pessoas</a></li>
                    <li><a href='/autores'>Autores</a></li>
                    <li><a href='/pessoasjuridicas'>Pessoa Juridica</a></li>
                    <li><a href='/pessoasfisicas'>Pessoa Fisica</a></li>
                    <li><a href='/artigoscientificos'>Artigo Cientifico</a></li>
                </ul>
            """
    return HttpResponse(html)

"""Listando todos os Eventos"""
def listaEventos(request):
    html = "<h1>Lista de Eventos </h1>"
    lista = Evento.objects.all()
    for e in lista:
        html += '<li> {} </br> {} </br>: {} </br> {} </br> {} </br> {} <br>  {} <br>  {} <br>  {} <br>  {} <br>  {}</li></br></br>'.format(
            e.nome, e.eventoPrincipal, e.sigla, e.dataEHoraDeInicio, e.palavrasChave, e.logotipo, e.realizador, e.cidade, e.uf, e.endereco, e.cep)
    return HttpResponse(html)


"""Listando Evento por parametro ID"""
def xEvento(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    e = Evento.objects.get(id=id)
    html += '<li> {} </br> {} </br>: {} </br> {} </br> {} </br> {} <br>  {} <br>  {} <br>  {} <br>  {} <br>  {}</li></br></br>'.format(
            e.nome, e.eventoPrincipal, e.sigla, e.dataEHoraDeInicio, e.palavrasChave, e.logotipo, e.realizador, e.cidade, e.uf, e.endereco, e.cep)
  	

    return HttpResponse(html)



    """Listando todos os Eventos"""
def listaPessoas(request):
    html = "<h1>Lista de Eventos </h1>"
    lista = Pessoa.objects.all()
    for p in lista:
        html += '<li> {} </br> {}</li></br></br>'.format(
            p.nome, p.email)
    return HttpResponse(html)


"""Listando Evento por parametro ID"""
def xPessoa(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    p = Pessoa.objects.get(id=id)
    html += '<li> {} </br> {}</li></br></br>'.format(
            p.nome, p.email)
  	

    return HttpResponse(html)



    """Listando todos os Autor"""
def listaAutores(request):
    html = "<h1>Lista de Eventos </h1>"
    a = Autor.objects.all()
    for a in lista:
        html += '<li> {} </br> {} </br>: {}</li></br></br>'.format(
            a.nome, a.email, a.curriculo, a.artigos)
    return HttpResponse(html)


"""Listando Autor por parametro ID"""
def xAutor(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    a = Autor.objects.get(id=id)
    html += '<li> {} </br> {} </br> {}</br> {} </li></br></br>'.format(
            a.nome, a.email, a.curriculo, a.artigos)

    return HttpResponse(html)


def listaPessoasJuridicas(request):
    html = "<h1>Lista de Eventos </h1>"
    a = PessoaJuridica.objects.all()
    for a in lista:
        html += '<li> {} </br> {} </br>: {}</br> {}</li></br></br>'.format(
            pj.nome, pj.email, pj.cnpj, pj.razaosocial)

    return HttpResponse(html)


"""Listando Autor por parametro ID"""
def xPessoasJuridica(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    pj= PessoaJuridica.objects.get(id=id)
    html += '<li> {} </br> {} </br>: {} </br> {}</li></br></br>'.format(
            pj.nome, pj.email, pj.cnpj, pj.razaosocial)

    return HttpResponse(html)

def listaPessoasFisicas(request):
    html = "<h1>Lista de Eventos </h1>"
    pf = PessoaFisica.objects.all()
    for a in lista:
        html += '<li> {} </br> {} </br>: {}</li></br></br>'.format(
            pf.nome, pf.email, pf.cpf)

    return HttpResponse(html)


"""Listando Autor por parametro ID"""
def xPessoaFisica(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    pf= PessoaFisica.objects.get(id=id)
    html += '<li> {} </br> {}</li></br></br>'.format(
            pf.nome, pf.email, pf.cpf)

    return HttpResponse(html)


def listaArtigos(request):
    html = "<h1>Lista de Eventos </h1>"
    a = Artigo.objects.all()
    for a in lista:
        html += '<li> {} </br> {} </br>: {}</li></br></br>'.format(
            a.nome, a.autores, a.evento)

    return HttpResponse(html)


"""Listando Autor por parametro ID"""
def xArtigo(request, id):
    html = "<h1>Tipo de Atividades por ID</h1>"
    a= Artigo.objects.get(id=id)
    html += '<li> {} </br> {} </br>: {}</li></br></br>'.format(
            a.nome, a.autores, a.evento)

    return HttpResponse(html)


