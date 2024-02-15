from django.urls import path  # Importa a função 'path' do módulo 'django.urls'
from .views import index, contato, produto  # Importa as funções 'index', 'contato' e 'produto' do módulo 'views' no mesmo diretório

urlpatterns = [  # Define uma lista de padrões de URL para o seu aplicativo Django
    path('', index, name='index'),  # Mapeia a URL raiz ('') para a função de view 'index' e dá a ela o nome 'index'
    path('contato', contato, name = 'contato'),  # Mapeia a URL 'contato' para a função de view 'contato' e dá a ela o nome 'contato'
    path('produto/<int:pk>', produto, name='produto'),  # Mapeia a URL 'produto/<int:pk>' para a função de view 'produto' e dá a ela o nome 'produto'. '<int:pk>' é um parâmetro de URL que aceita um inteiro e o passa para a função de view como argumento.
]
