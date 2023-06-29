from django.shortcuts import render
from django.http import JsonResponse
from database.models import Usuario,Funcionario
from  .constructor import logon,miss_senha
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from gestao_estoque.views import msgerror


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            decode_json = request.body.decode('utf-8')
            registro_usuario = json.loads(decode_json)
            log = logon(registro_usuario["login"],registro_usuario["senha"])
            if Usuario.objects.filter(login = log.login,senha = log.senha).exists():
                return JsonResponse({"situacao":"usuario encontrado com sucesso"})
            else:
                return JsonResponse({"situacao":"usuario nao encontrado"})
        except Exception as error:
            return JsonResponse({"error":str(error)})
    else:
        return JsonResponse(msgerror)
    
def loginfunc(request):
    if request.method == 'POST': 
        try:
            decode_json = request.body.decode('utf-8')
            registro_funcionario = json.loads(decode_json)
            log = logon(registro_funcionario["login"],registro_funcionario["senha"])
            if Funcionario.objects.filter(cpf_funcionario = log.login,senha_func = log.senha).exists():
                return JsonResponse({"situacao":"funcionario encontrado com sucesso"})
            else:
                return JsonResponse({"situacao":"funcionario nao encontrado"})
        except Exception as error:
            return JsonResponse({"error":str(error)})
    else:
        return JsonResponse(msgerror)

@csrf_exempt
def esquecisenha(request):
    if request.method == "POST":
        try:
            decode_json = request.body.decode('utf-8')
            registro_usuario = json.loads(decode_json)
            miss = miss_senha(registro_usuario["cpf"],
                              registro_usuario["email"],
                              registro_usuario["senha"],
                              registro_usuario["login"])
            
            if Usuario.objects.filter(cpf = miss.cpf,login = miss.login,email = miss.email).exists():
                user = Usuario.objects.get(cpf = miss.cpf)
                user.senha = miss.senha
                user.save()
                return JsonResponse({"situacao" : "a senha foi alterada"})
            else:
                return JsonResponse({"situacao" : "o usuario nao foi encontrado entao a senha nao foi alterada",})
        except Exception as error:
            return JsonResponse({"error" : str(error)})
    else:
        return JsonResponse(msgerror)
