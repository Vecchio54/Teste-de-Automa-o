from django.urls import reverse_lazy
from switch.models import Switch
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.utils import timezone


class CadastroSW(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Switch
    fields = ['hostname', 'ip']
    template_name = 'switch/cadastro.html'
    success_url = reverse_lazy('lista_sw')
    success_message = 'Switch cadastrado com sucesso!'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.data = timezone.now()
        return super(CadastroSW, self).form_valid(form)

class ListaSW(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Switch
    template_name = 'switch/lista.html'
    paginate_by = 5

    def get_queryset(self) :
        sw_name = self.request.GET.get('search')
        if sw_name:
           sw = Switch.objects.filter(hostname__icontains=sw_name)

        else:
            sw = Switch.objects.all()

        return sw

class EditaSW(SuccessMessageMixin, GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('denied')
    group_required = [u'adm']
    model = Switch
    fields = ['hostname', 'ip']
    template_name = 'switch/cadastro.html'
    success_url = reverse_lazy('lista_sw')
    success_message = 'Switch cadastrado com sucesso!'






