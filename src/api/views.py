# Create your views here.
import json
from django.http import JsonResponse
from .models import Funcionario, Perfil, Curriculo
from .serializers import FuncionarioSerializer, PerfilSerializer, CurriculoSerializer

def health(request):
    return JsonResponse({"mensagem": "ok"}, safe=False)


def funcionario_info(request):
    """View Funcionário"""
    query_params = request.GET

    if request.method == 'GET':
        lista_funcionario = Funcionario.objects.all().values()
        serializer = FuncionarioSerializer(lista_funcionario, many=True)
        return JsonResponse({"mensagem": serializer.data})

    if request.method == 'POST':
        data = json.loads(request.body)

        funcionario = Funcionario()
        funcionario.nome = data.get("nome")
        funcionario.sobrenome = data.get("sobrenome")
        funcionario.funcao = data.get("funcao")
        funcionario.email = data.get("email")
        funcionario.ano_nascimento = data.get("ano_nascimento")
        existe_funcionario = Funcionario.objects.filter(email=funcionario.email).count()
        if existe_funcionario:
            return JsonResponse({"mensagem": "O usuário já foi cadastrado"})

        funcionario.save()
        serilizer = FuncionarioSerializer(funcionario, many=False)
        return JsonResponse(serializer.data)
        
    if request.method == 'DELETE':
        existe_email= query_params.get('email')

        if existe_email:
            existe_funcionario = Funcionario.objects.filter(email=existe_email).first()

            if existe_funcionario:
                serializer = FuncionarioSerializer(existe_funcionario, many=False)
                existe_funcionario.delete()
                return JsonResponse({"Objeto": serializer.data})
        return JsonResponse({"mensagem": "O usuário não encontrado"})

    if request.method == 'PUT':
        data = json.loads(request.body)
        email = query_params.get('email')

        existe_email = Funcionario.objects.filter(email=data.get('email')).count()
        if existe_email:
            return JsonResponse({'mensagem': 'Usuário já existe'})

        funcionario = Funcionario.objects.filter(email=email).first()
        if funcionario:
            funcionario.ano_nascimento = data.get('ano_nascimento')
            funcionario.nome = data.get('nome')
            funcionario.sobrenome = data.get('sobrenome')
            funcionario.email = data.get('email')
            funcionario.funcao = data.get('funcao')
            funcionario.save()
            serializer = FuncionarioSerializer(funcionario, many=False)
            return JsonResponse(serializer.data)

        return JsonResponse({'mensagem': 'Usuário não encontrado'})

    return JsonResponse({"mensagem": "Método inválido"})


def perfil_info(request):
    query_params = request.GET

    if request.method == 'GET':
        lista_perfis = Perfil.objects.all().values()
        serializer = PerfilSerializer(lista_perfis, many=True)

        return JsonResponse({'perfis': serializer.data})

    if request.method == 'POST':
        data = json.loads(request.body)

        perfil = Perfil()
        perfil.nome = data.get('nome')
        perfil.sobrenome = data.get('sobrenome')
        perfil.avatar = data.get('avatar')
        perfil.email = data.emai('email')
        perfil.celular = data.celular = ('celular')

        existe_perfil = Perfil.objects.filter(email=perfil.email).count()
        if existe_perfil:
            return JsonResponse({'mensagem': 'O usuário já existe'})

        perfil.save()                                 
        serializer = PerfilSerializer(perfil, many=False)
        return JsonResponse({'Objeto': serializer.data})


    if request.method == 'PUT':
        data = json.loads(request.body)
        existe_perfil = Perfil.objects.filter(email=query_params.get('email')).count()

        if existe_perfil:
            perfil = Perfil()
            perfil.nome = data.get('nome')
            perfil.sobrenome = data.get('sobrenome')
            perfil.avatar = data.get('avatar')
            perfil.email = data.emai('email')
            perfil.celular = data.celular = ('celular')

            perfil.save()
            serializer = PerfilSerializer(perfil, many=False)
            return JsonResponse({'objeto': serializer.data})

        return JsonResponse({'mensagem': 'Email não existe'})

        if existe_perfil:
            perfil = Perfil()

    if request.method == 'DELETE':
        existe_email = query_params.get('email')

        perfil = Perfil.objects.filter(email=existe_email).first()

        if perfil:
            perfil.delete()
            return JsonResponse({'mensagem': 'objeto deletado'})
    

        return JsonResponse({'mensagem': 'objeto não emcontrado'})        
        



def curriculo_info(request):
    """View da model Perfil."""

    query_params = request.GET

    if request.method == 'GET':
        return JsonResponse({'mensagem': 'Curriculo OK'})


    if request.method == 'POST':
        data = json.loads(request.body)

    
    if request.method == 'PUT':
        data = json.loads(request.body)

    if request.method == 'DELETE':
        return JsonResponse({'mensagem': 'objeto deletado'})
        