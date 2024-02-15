from django.contrib import admin  # Importa o módulo de administração do Django

from .models import Produto, Cliente  # Importa os modelos Produto e Cliente do módulo 'models' no mesmo diretório

class ProdutoAdmin(admin.ModelAdmin):  # Define uma classe de administração personalizada para o modelo Produto
    list_display = ('nome', 'preco', 'estoque')  # Define os campos que serão exibidos na lista de produtos na interface de administração

class ClienteAdmin(admin.ModelAdmin):  # Define uma classe de administração personalizada para o modelo Cliente
    list_display = ('nome', 'sobrenome', 'email')  # Define os campos que serão exibidos na lista de clientes na interface de administração

admin.site.register(Produto, ProdutoAdmin)  # Registra o modelo Produto e sua classe de administração personalizada no site de administração
admin.site.register(Cliente, ClienteAdmin)  # Registra o modelo Cliente e sua classe de administração personalizada no site de administração
