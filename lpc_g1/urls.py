"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from evento.views import inicio, listaEventos, xEvento, listaPessoas, xPessoa, listaAutores, xAutor, listaPessoasJuridicas, xPessoasJuridica, listaPessoasFisicas, xPessoaFisica, listaArtigos, xArtigo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^evetos/', listaEventos, name='listaEventos'),
    url(r'^eventosx/([0-9])$', xEvento),
    url(r'^pessoas/', listaPessoas, name='listaPessoas'),
    url(r'^pessoasx/([0-9])$', xPessoa),
    url(r'^autores/', listaAutores, name='listaAutores'),
    url(r'^autoresx/([0-9])$', xAutor),
    url(r'^pessoasjuridicas/', listaPessoasJuridicas, name='listaPessoasJuridicas'),
    url(r'^pessoasjuridicasx/([0-9])$', xPessoasJuridica),
    url(r'^pessoasfisicas/', listaPessoasFisicas, name='listaPessoasFisicas'),
    url(r'^pessoasfisicasx/([0-9])$', xPessoaFisica),
	url(r'^artigos/', listaArtigos, name='listaArtigos'),
    url(r'^artigosx/([0-9])$', xArtigo),



   
]
