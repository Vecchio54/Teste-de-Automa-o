from django.db import models
from django.utils import timezone
from switch.models import Switch
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class Computer(models.Model):

     PORTA_CHOICES = [

             ('', "selecione a porta"),
             ('Gi0/0', 'Gi0/0'),
             ('Gi0/1', 'Gi0/1'),
             ('Gi0/2', 'Gi0/2'),
             ('Gi0/3', 'Gi0/3'),
             ('gi1/0', 'gi1/0'),
             ('gi1/1', 'gi1/1'),
             ('gi1/2', 'Gi1/2'),
             ('gi1/3', 'Gi1/3'),
     ]

     DADOS_CHOICES = [

             ('', "seleciona rede de dados"),
             ('20', '20-Dados Administração'),
             ('15', '15-Dados Atendimento'),
     ]

     VOICE_CHOICES = [

            ('', "seleciona rede de dados"),
            ('21', '21-voz Administração'),
            ('16', '16-voz Atendimento'),
     ]

     hostname = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Hostname')
     switch = models.ForeignKey(Switch, on_delete=models.PROTECT, blank=False, verbose_name= 'Switch')
     dados = models.CharField(max_length=4, null=True, blank=True, choices=DADOS_CHOICES)
     voz = models.CharField(max_length=4, null=True, blank=True, choices=VOICE_CHOICES)
     porta = models.CharField(max_length=8, null=False, blank=False, choices=PORTA_CHOICES, verbose_name='Porta Switch')
     usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
     data = models.DateTimeField(default=timezone.now)
     history = HistoricalRecords()

def __str__(self):
    return self.hostname

class Meta:
    ordering = ['hostname']
