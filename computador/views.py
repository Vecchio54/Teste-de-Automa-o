from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from .models import Computer
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .automa import altera_vlan
from django.http import HttpResponseRedirect

class CadastroPC(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Computer
    fields = ['hostname', 'switch', 'porta', 'dados', 'voz']
    template_name = 'computador/cadastro_pc.html'
    success_url = reverse_lazy('lista_pc')
    success_message = 'Computador cadastrado com sucesso!'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.data = timezone.now()
        return super().form_valid(form)



class ListaPC(LoginRequiredMixin, GroupRequiredMixin, ListView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm', u'suporte']
    model = Computer
    template_name = 'computador/lista_pc.html'
    paginate_by = 5

    def get_queryset(self):
        pc_txt_nome = self.request.GET.get('search')

        if pc_txt_nome:
            pc = Computer.objects.filter(hostnome__icontains=pc_txt_nome)
        else:
            pc = Computer.objects.all()

        return pc

class EditaPC(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Computer
    fields = ['hostname', 'switch', 'porta', 'dados', 'voz']
    template_name = 'computador/cadastro_pc.html'
    success_url = reverse_lazy('lista_pc')
    success_message = 'Computador editado com sucesso!'



class AlteraVlan(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm', u"suporte"]
    model = Computer
    fields = ['dados', 'voz']
    template_name = 'computador/cadastro_pc.html'
    success_url = reverse_lazy('lista_pc')
    success_message = 'Vlan alterada com sucesso!'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.data = timezone.now()
        bloqueado = reverse_lazy('denied')

        if altera_vlan(ip_sw=form.instance.switch.ip, port_sw=form.instance.porta,
                       v_dados=form.instance.dados, v_voz=form.instance.voz):
            return super().form_valid(form)
        else:
            return HttpResponseRedirect(bloqueado)




