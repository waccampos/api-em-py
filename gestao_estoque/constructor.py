
class excluirproduto:
    def __init__(self,idp,cpf,senha):
        self.idp = idp
        self.cpf = cpf
        self.senha = senha
        
class produto:
    def __init__(self,qtd_estoque,descricao,nome,preco,categoria,tipo):
        self.qtd_estoque = qtd_estoque
        self.descricao = descricao
        self.nome = nome 
        self.preco = preco
        self.categoria = categoria
        self.tipo = tipo