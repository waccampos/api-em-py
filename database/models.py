from django.db import models

class Usuario(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11)
    nome = models.TextField()
    senha = models.TextField()
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    login = models.TextField(unique=True)
    
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    qtd_estoque = models.IntegerField()
    descricao = models.TextField()
    nome = models.CharField(max_length=100,unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

class Estoque(models.Model):
    setor = models.TextField()
    corredor = models.IntegerField()
    prateleira = models.IntegerField(primary_key=True)
    id_produto = models.OneToOneField(Produto, unique=True,on_delete=models.CASCADE)

class Funcionario(models.Model):
    cpf_funcionario = models.CharField(primary_key=True, max_length=11)
    nome_funcionario = models.TextField()
    cargo = models.CharField(max_length=30)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria = models.FloatField()
    senha_func = models.CharField(max_length=30,null=False)
    tipo_acesso = models.TextField(null=False)
    
class FolhaPonto(models.Model):
    cpf_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_entrada = models.TextField()
    data_saida = models.TextField()

class RegistroVendas(models.Model):
    id_venda = models.AutoField(primary_key=True)
    cpf_usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    produto = models.TextField()
    quantidade = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now=True)
    
class RegistroCompra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    cpf_funcionario = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)
    produto = models.TextField()
    quantidade = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now=True)


    
    