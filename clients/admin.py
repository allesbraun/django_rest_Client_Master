from django.contrib import admin

from clients.models import Client


class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','cpf', 'rg', 'cellphone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'cpf', )
    list_filter = ('active', )
    list_editable = ('active', )
    list_per_page = 10
    ordering = ('name', )

admin.site.register(Client, Clients)

