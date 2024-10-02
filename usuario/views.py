from django.shortcuts import render

def acesso_negado(request):
    return render(request, 'usuario/acesso_negado.html' )
