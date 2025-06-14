from django.contrib import admin

from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefono')
    search_fields = ('nome', 'email', 'telefono')
