from django.contrib import admin
from evento.models import Evento, Pessoa, Autor, PessoaFisica, PessoaJuridica, EventoCientifico, ArtigoCientifico


admin.site.register(Evento)
admin.site.register(Pessoa)
admin.site.register(Autor)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)
