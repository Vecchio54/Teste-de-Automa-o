from django.urls import path
from .views import CadastroSW, ListaSW, EditaSW

urlpatterns = [
    path('cadastro-switch/', CadastroSW.as_view(), name='cadastro_sw'),
    path('lista-switch/', ListaSW.as_view(), name='lista_sw'),
    path("edita-switch/<int:pk>", EditaSW.as_view(), name='edita_sw'),

]
