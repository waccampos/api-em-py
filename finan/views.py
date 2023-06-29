from django.shortcuts import render
from django.http import JsonResponse
import json
from .constructor import venda,compra
from database.models import Produto,RegistroVendas,Usuario,Funcionario,RegistroCompra
from django.views.decorators.csrf import csrf_exempt
from gestao_estoque.views import msgerror


@csrf_exempt
def vender(request):
    lista_produto = list()
    lista_qtd = list()
    lista_unid = list()
    total = 0
    if request.method == 'POST':
        try:
            decode_json = request.body.decode('utf-8')
            registro_venda = json.loads(decode_json)
            carrinho = venda(registro_venda["cpf"],
                            registro_venda["lista"],)
            
            if Usuario.objects.filter(cpf = carrinho.cpf).exists():
                usuario = Usuario.objects.get(cpf = carrinho.cpf)
                for i in carrinho.lista:
                    if Produto.objects.filter(nome = i["nome"]).exists():
                        prod = Produto.objects.get(nome = i["nome"])
                        if i["qtd"] <= prod.qtd_estoque:
                            prod.qtd_estoque =  prod.qtd_estoque - i["qtd"]
                            total = total + (i["qtd"] * prod.preco)
                            lista_produto.append(prod.nome)
                            lista_unid.append(float(prod.preco))
                            lista_qtd.append(i["qtd"])
                            prod.save()
                            
                        else:
                            return JsonResponse({"situacao": "qtd invalida"})
                    else:
                            return JsonResponse({"situacao": "fruta invalida"})
                    
                registro_venda = RegistroVendas(cpf_usuario = usuario,produto = lista_produto,quantidade = lista_qtd,valor_total = total)
                registro_venda.save()
                            
                return JsonResponse({"success": "Compra realizada com sucesso!",
                                    "id da compra":registro_venda.id_venda,
                                    "cpf":str(carrinho.cpf),
                                    "produtos  " : str(lista_produto),
                                    "preço unidade": str(lista_unid),
                                    "quantidade" : str(lista_qtd),
                                    "valor unidade":str(lista_unid),
                                    "valor total":str(total)})
                                     
            else:
                return JsonResponse({"situacao":"cpf invalido!"})
        except Exception as error:
            return JsonResponse({"error":str(error)})
    else:
        return JsonResponse(msgerror)

@csrf_exempt
def comprar(request):
    lista_produto = list()
    lista_qtd = list()
    total = 0
    if request.method == 'PUT':
        try:
            decode_json = request.body.decode('utf-8')
            registro_compra = json.loads(decode_json)
            comprar = compra(registro_compra["cpf"],
                             registro_compra["senha"],
                             registro_compra["tipo_acesso"],
                             registro_compra["lista"])
            
            if Funcionario.objects.filter(cpf_funcionario = comprar.cpf,senha_func = comprar.senha).exists():
                funcionario1 = Funcionario.objects.get(cpf_funcionario = comprar.cpf)     
                if funcionario1.tipo_acesso == 'adm' or funcionario1.tipo_acesso == "padrao":
                    for i in comprar.lista:
                        if Produto.objects.filter(nome = i["nome"]).exists():
                            produto = Produto.objects.get(nome = i["nome"])
                            produto.qtd_estoque = produto.qtd_estoque + i["qtd"]
                            lista_produto.append(produto.nome)
                            lista_qtd.append(i["qtd"])
                            total = total + i["valor"]
                            produto.save()
                          
                            
                    registro_venda = RegistroCompra(cpf_funcionario = funcionario1,
                                                            produto = lista_produto,
                                                            quantidade = lista_qtd,
                                                            valor_total = total)
                    registro_venda.save()
                        
                    return JsonResponse({"success": "Compra realizada com sucesso!",
                                "id da compra": registro_venda.id_compra,
                                "cpf       ": str(comprar.cpf),
                                "produtos  " : str(lista_produto),
                                "quantidade" : str(lista_qtd),
                                "valor total": str(total)})
                        

                else:
                    return JsonResponse({"situacao":"acesso negado"})    
            else:
                return JsonResponse({"situacao":"login ou senha incorreta ou nome do produto incorreto"})    
              
        except Exception as error:
            return JsonResponse({"error":str(error)})
    else:
        return JsonResponse(msgerror)
    