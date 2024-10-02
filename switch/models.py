from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User


class Switch(models.Model):
    hostname = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Hostname')
    ip = models.GenericIPAddressField(unique=True, blank=False, verbose_name='IP')
    data = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario')
    history = HistoricalRecords()

    class Meta:
        ordering = ['hostname']

    def __str__(self):
        return self.hostname
