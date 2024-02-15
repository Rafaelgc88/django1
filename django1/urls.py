"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import path, include  # Importa as funções 'path' e 'include' do módulo de URLs do Django
from django.conf.urls import handler404, handler500  # Importa os manipuladores de erro 404 e 500 do módulo de configuração de URLs do Django
from core import views  # Importa o módulo de views do diretório 'core'

urlpatterns = [  # Define uma lista de padrões de URL para o seu aplicativo Django
    path('admin/', admin.site.urls),  # Mapeia a URL 'admin/' para as URLs do site de administração do Django
    path('', include('core.urls')),  # Inclui as URLs do módulo 'core.urls' na URL raiz ('')
]

handler404 = views.error404  # Define a view 'error404' do módulo 'core.views' como o manipulador de erro 404
handler500 = views.error500  # Define a view 'error500' do módulo 'core.views' como o manipulador de erro 500

