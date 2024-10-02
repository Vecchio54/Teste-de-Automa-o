from django.contrib import admin
from .models import Computer
from simple_history.admin import SimpleHistoryAdmin

class ComputerAdmin(SimpleHistoryAdmin):
    list_display = ('hostname',)
    list_filter = ('hostname',)
    search_fields = ('hostname',)
    list_per_page = 10

admin.site.register(Computer, ComputerAdmin)



