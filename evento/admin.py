from django.contrib import admin
from evento.models import TipoAtividade, Atividade, Evento


admin.site.register(Evento)
admin.site.register(Pessoa)
admin.site.register(Autor)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(EventoCientifico)