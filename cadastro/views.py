from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from database.models import Usuario,Produto,RegistroVendas,FolhaPonto,Funcionario,Estoque
import json
from .constructor import usuario
from django.views.decorators.csrf import csrf_exempt
from gestao_estoque.views import msgerror


def excluirtudo(request):
    if request.method == 'GET':
        try:
            Usuario.objects.all().delete()
            Produto.objects.all().delete()
            RegistroVendas.objects.all().delete()
            FolhaPonto.objects.all().delete()
            Funcionario.objects.all().delete()
            transaction.commit()
            return JsonResponse({"excluido":"ok"})
        except Exception as erroe:
            return JsonResponse({"error":str(erroe)}) 
    else:
        return JsonResponse({"excluido":"nao"})

@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'POST':
        try:
            decode_json = request.body.decode('utf-8')
            registro_usuario = json.loads(decode_json)
            user = usuario( registro_usuario["cpf"],
                            registro_usuario["nome"],
                            registro_usuario["senha"],
                            registro_usuario["idade"],
                            registro_usuario["email"],
                            registro_usuario["login"])
                  
            if  len(user.cpf) == 11:
                
                novo_usuario = Usuario( cpf = user.cpf, 
                                        nome = user.nome, 
                                        senha = user.senha, 
                                        idade = user.idade,
                                        email = user.email,
                                        login = user.login)
                
                if Usuario.objects.filter(cpf = registro_usuario["cpf"]).exists():
                    return JsonResponse({"error":"ja existe esse cpf no banco de dados"})
                else:
                    novo_usuario.save()
                    return JsonResponse({"status": "Cadastro realizado com sucesso"})
            else:
                return JsonResponse({"error":"cpf invalido"})                
        except Exception as error:
            return JsonResponse({"error":str(error)})
    else:
        return JsonResponse(msgerror)
        

   
    