from django.urls import path
from .views import CadastroPC, ListaPC, EditaPC, AlteraVlan

urlpatterns = [
    path('cadastro-pc/', CadastroPC.as_view(), name='cadastro_pc'),
    path('lista-pc/', ListaPC.as_view(), name='lista_pc'),
    path('edita-pc/<int:pk>', EditaPC.as_view(), name='edita_pc'),
    path("editar-vlan/<int:pk>", AlteraVlan.as_view(), name='edita_vlan'),
]
