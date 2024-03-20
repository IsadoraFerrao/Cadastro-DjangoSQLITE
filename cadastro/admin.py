from django.contrib import admin
from cadastro.models import Cadastro

@admin.register(Cadastro)

class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']