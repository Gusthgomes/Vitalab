from django.contrib import admin
from .models import PedidosExames, SolicitacaoExame, TiposExames, AcessoMedico

admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)
admin.site.register(TiposExames)
admin.site.register(AcessoMedico)
