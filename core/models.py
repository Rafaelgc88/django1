from django.db import models  # Importa o módulo de modelos do Django

class Produto(models.Model):  # Define uma classe de modelo Produto que herda de models.Model
    nome = models.CharField('Nome', max_length=100)  # Define um campo de caracteres com um máximo de 100 caracteres para o nome do produto
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)  # Define um campo decimal para o preço do produto com 2 casas decimais e um máximo de 8 dígitos
    estoque = models.IntegerField('Quantidade em Estoque')  # Define um campo inteiro para a quantidade de produtos em estoque

    def __str__(self):  # Define o método __str__ para retornar o nome do produto quando o objeto Produto é convertido em string
        return self.nome

class Cliente(models.Model):  # Define uma classe de modelo Cliente que herda de models.Model
    nome = models.CharField('Nome', max_length=100)  # Define um campo de caracteres com um máximo de 100 caracteres para o nome do cliente
    sobrenome = models.CharField('Sobrenome', max_length=100)  # Define um campo de caracteres com um máximo de 100 caracteres para o sobrenome do cliente
    email = models.EmailField('E-mail', max_length=100)  # Define um campo de e-mail para o e-mail do cliente com um máximo de 100 caracteres

    def __str__(self):  # Define o método __str__ para retornar o nome completo do cliente quando o objeto Cliente é convertido em string
        return f'{self.nome} {self.sobrenome}'
