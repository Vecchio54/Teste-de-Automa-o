from django.contrib import admin
from .models import Switch
from simple_history.admin import SimpleHistoryAdmin

class SwitchAdmin(SimpleHistoryAdmin):
    list_display = ('hostname', "ip", "usuario", "data",)
    list_filter = ('hostname', "ip", "usuario", "data",)
    search_fields = ('hostname', "ip", "usuario", "data",)
    list_per_page = 10

admin.site.register(Switch, SwitchAdmin)


