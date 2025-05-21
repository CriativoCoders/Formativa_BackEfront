from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Professor

@api_view(['POST'])
def registrar(request):
    nome = request.data.get('nome')
    email = request.data.get('email')
    indentificacao = request.data.get('indentificacao')
    telefone = request.data.get('telefone') 
    data_nascimento = request.data.get('data_nascimento')
    data_contratacao = request.data.get('data_contratacao')

    if not nome or not indentificacao or not email:
        return Response({'Erro': 'Os campos nome, email e indentificacao são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

    if Professor.objects.filter(email=email).exists():
        return Response({'Erro': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

    professor = Professor.objects.create_user(
        username=email,  # obrigatório para AbstractUser
        nome=nome,
        email=email,
        indentificacao=indentificacao,
    )

    return Response({'Mensagem': 'O usuário foi cadastrado com sucesso'}, status=status.HTTP_201_CREATED)

