from django.shortcuts import render
import json
from django.http import JsonResponse
from .constructor import funcionario
from gestao_estoque.views import msgerror
from database.models import Funcionario,FolhaPonto
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cadastro_func(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        registro_funcionario = json.loads(decode_json)
        func = funcionario(registro_funcionario["cpf"],
                           registro_funcionario["nome"],
                           registro_funcionario["cargo"],
                           registro_funcionario["salario"],
                           registro_funcionario["carga"],
                           registro_funcionario["senha"],
                           registro_funcionario["tipo_acesso"]
                           )
        if Funcionario.objects.filter(cpf_funcionario = func.cpf).exists():   
            return JsonResponse({"situacao" : "funcionario ja cadastrado"})
        
        else:
            novo_func = Funcionario(cpf_funcionario = func.cpf,
                                    nome_funcionario = func.nome,
                                    cargo = func.cargo,
                                    salario = func.salario,
                                    carga_horaria = func.carga_horaria,
                                    senha_func = func.senha,
                                    tipo_acesso = func.tipo)
            novo_func.save()
            f = FolhaPonto(cpf_funcionario = novo_func)
            f.save()
            return JsonResponse({"situacao" : "sucesso"})
    else:
        return JsonResponse(msgerror)

