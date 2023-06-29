from django.shortcuts import render
from django.http import JsonResponse
from database.models import FolhaPonto,Funcionario
from gestao_estoque.views import msgerror
from datetime import datetime
import json
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def folhapontochegada(request):
    if request.method == 'POST':
        try:
            decode_json = request.body.decode('utf-8')
            registro_ponto = json.loads(decode_json)
            
            if Funcionario.objects.filter(cpf_funcionario = registro_ponto["cpf"]).exists():
                f = Funcionario.objects.get(cpf_funcionario = registro_ponto["cpf"])
                func = FolhaPonto.objects.get(cpf_funcionario=f)
                
                func.data_entrada = datetime.now()
                func.save()
                return JsonResponse({"situacao": "Funcionário registrou entrada com sucesso."})
            else:
                return JsonResponse({"situacao": "Funcionário não encontrado."})
        except Exception as error:
            return JsonResponse({"error": str(error)})
    else:
        return JsonResponse({"situacao": "Método de requisição não suportado."})

@csrf_exempt
def folhapontosaida(request):
    if request.method == 'POST':
       try:
            decode_json = request.body.decode('UTF-8')
            registro_ponto = json.loads(decode_json)
            
            if Funcionario.objects.filter(cpf_funcionario = registro_ponto["cpf"]).exists():
                f = Funcionario.objects.get(cpf_funcionario = registro_ponto["cpf"])
                func = FolhaPonto.objects.get(cpf_funcionario=f)

                func.data_saida = datetime.now()
                func.save()
                return JsonResponse({"situacao": "Funcionário registrou saida com sucesso."})
            else:
                return JsonResponse({"situacao": "Funcionário nao encontrado."})
                        
       except Exception as error:
           return JsonResponse({"error": error})
