from django.contrib import admin
from .models import Ordine

@admin.register(Ordine)
class OrdineAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'prodotto', 'quantita', 'data_ordine', 'stato')
    list_filter = ('stato',)
    search_fields = ('cliente__nome', 'prodotto__nome')
