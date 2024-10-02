
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import acesso_negado
from home.views import home

def login(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        from django.contrib.auth.views import LoginView
        return LoginView.as_view(template_name='usuario/usuario.html')(request)
        
urlpatterns = [
    path('', login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path('denied', acesso_negado, name='denied'),
]
