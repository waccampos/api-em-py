class compra:
    def __init__(self,cpf,senha,tipo_acesso,lista):
        self.cpf = cpf
        self.senha = senha
        self.tipo_acesso = tipo_acesso
        self.lista = lista
        
class venda:
    def __init__(self,cpf,lista):
        self.lista = lista
        self.cpf = cpf