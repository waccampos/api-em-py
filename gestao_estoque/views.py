from django.shortcuts import render
from django.http import JsonResponse
import json
from .constructor import excluirproduto,produto
from database.models import Produto,Funcionario,Estoque
from django.views.decorators.csrf import csrf_exempt

msgerror = {"error" : "Metodo nao permitido", "dica" : "use o metodo post para adicionar um usuario no bd"}

@csrf_exempt
def cadastrar_produto(request):
    if request.method == 'POST':
        try:
            decode_json = request.body.decode('utf-8')
            registro_produto = json.loads(decode_json)
            prod = produto(registro_produto["qtd_estoque"],
                            registro_produto["descricao"],
                            registro_produto["nome"],
                            registro_produto["preco"],
                            registro_produto["categoria"],
                            registro_produto["tipo"])
            
            novo_produto = Produto(qtd_estoque=prod.qtd_estoque,
                                   descricao=prod.descricao,
                                   nome=prod.nome,
                                   preco=prod.preco,
                                   categoria=prod.categoria,
                                   tipo=prod.tipo)
            
            if Produto.objects.filter(nome = prod.nome).exists():
                return JsonResponse({"error" : "ja existe esta fruta no banco de dados"})
            else:
                novo_produto.save()
                return JsonResponse({"status" : "Cadastro realizado com sucesso",})
        except Exception as error:
            return JsonResponse({"error":str(error)})
    else:
        return JsonResponse(msgerror)
    
@csrf_exempt
def quantidadeprod(request): 
    if request.method == "GET":
        try:
            lista = []
            produtos = Produto.objects.all()  
            for i in produtos:
                lista.append({"id_produto" : str(i.id_produto),
                              "qtd_estoque": str(i.qtd_estoque),
                              "nome": str(i.nome),
                              "categoria" : str(i.categoria),
                              "preco": str(i.preco)
                              })
                
            return JsonResponse ({"produtos": lista})       
        except Exception as error:
            
            return JsonResponse(error)
    else:
        return JsonResponse(msgerror)

@csrf_exempt
def excluirprod(request):
    if request.method == 'DELETE':
        try:
            decode_json = request.body.decode('UTF-8')
            registro_excluir = json.loads(decode_json)
            login = excluirproduto(registro_excluir["id"],
                                   registro_excluir["cpf"],
                                   registro_excluir["senha"])
            if Funcionario.objects.filter(cpf_funcionario = login.cpf,senha_func = login.senha).exists() and Produto.objects.filter(id_produto = login.idp).exists():
                funcionario = Funcionario.objects.get(cpf_funcionario = login.cpf,senha_func = login.senha)
                if funcionario.tipo_acesso == 'adm':
                    dele = Produto.objects.get(id_produto = login.idp)
                    dele.delete()
                    return JsonResponse({"situacao":"produto excluido"})
                else:
                    return JsonResponse({"error": "vc nao tem acecsso a essa funcao"})
            else:
                return JsonResponse({"error": "funcionario ou id incorreto"})
            
        except Exception as error:
                return JsonResponse({"error":str(error)})
    else:
        return JsonResponse({"error": str(msgerror)})

@csrf_exempt
def estoque(request):
    if request.method == 'POST':
        try:
            decode_json = request.body.decode('utf-8')
            dados_estoque = json.loads(decode_json)
                
            setor = dados_estoque["setor"]
            corredor = dados_estoque["corredor"]
            prateleira = dados_estoque["prateleira"]
            id_produto = dados_estoque["id_produto"]
            if Estoque.objects.filter(id_produto = dados_estoque["id_produto"]).exists():
                return JsonResponse({"situacao":"produto ja cadastrado em um setor"})
            else:
                produto = Produto.objects.get(id_produto=id_produto)
                estoque = Estoque(setor=setor,
                                  corredor=corredor,
                                  prateleira=prateleira,
                                  id_produto=produto)
                estoque.save()
                return JsonResponse({"situacao": "Estoque cadastrado com sucesso."})
                
        except Exception as error:
            return JsonResponse({"error": str(error)})
    
    else:
        return JsonResponse({"situacao": "Método de requisição não suportado."})

def verestoque(request):
    if request.method == 'GET':
        try:
            lista = []
            estoques = Estoque.objects.all()
            for i in estoques:
                lista.append({"setor" : str(i.setor),
                              "corredor": str(i.corredor),
                              "prateleira": str(i.prateleira),
                              "id_produto" : str(i.id_produto)})
            
            return JsonResponse({"lista de estoque ":lista})
        except Exception as error:
            return JsonResponse({"error":str(error)})