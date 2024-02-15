from django.shortcuts import render  # Importa a função 'render' do Django
from django.shortcuts import get_object_or_404  # Importa a função 'get_object_or_404' do Django
from core.models import Produto  # Importa a classe 'Produto' do módulo 'models' no diretório 'core'
from django.http import HttpResponse  # Importa a classe 'HttpResponse' do Django
from django.template import loader  # Importa o 'loader' de templates do Django

def index(request):  # Define a view 'index'
    produtos = Produto.objects.all()  # Obtém todos os objetos 'Produto' do banco de dados
    context = {  # Define o contexto para o template
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)  # Renderiza o template 'index.html' com o contexto definido

def contato(request):  # Define a view 'contato'
    return render(request, 'contato.html')  # Renderiza o template 'contato.html'

def produto(request, pk):  # Define a view 'produto'
    prod = get_object_or_404(Produto, id=pk)  # Obtém o objeto 'Produto' com o id 'pk' ou retorna um erro 404 se não existir
    context = {  # Define o contexto para o template
        'produto': prod
    }
    return render(request, 'produto.html', context)  # Renderiza o template 'produto.html' com o contexto definido

def error404(request, ex):  # Define a view 'error404'
    template = loader.get_template('404.html')  # Carrega o template '404.html'
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)  # Retorna uma resposta HTTP com o template renderizado, o tipo de conteúdo e o status 404

def error500(request):  # Define a view 'error500'
    template = loader.get_template('500.html')  # Carrega o template '500.html'
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)  # Retorna uma resposta HTTP com o template renderizado, o tipo de conteúdo e o status 500

