from rest_framework import serializers
from .models import ProfessorGestor, Disciplina, Ambiente, Sala
from datetime import date

class ProfessorGestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorGestor
        fields = '__all__'

    def validate(self, data):
        # Validação de data de nascimento e contratação
        if data.get('Data_de_Nascimento') and data.get('Data_de_contratacao'):
            if data['Data_de_Nascimento'] > data['Data_de_contratacao']:
                raise serializers.ValidationError({"Data_de_Nascimento": "A data de nascimento não pode ser mais recente que a data de contratação."})

        # Validação de idade mínima (18 anos)
        if data.get('Data_de_Nascimento'):
            hoje = date.today()
            idade = hoje.year - data['Data_de_Nascimento'].year - ((hoje.month, hoje.day) < (data['Data_de_Nascimento'].month, data['Data_de_Nascimento'].day))
            if idade < 18:
                raise serializers.ValidationError({"Data_de_Nascimento": "O usuário deve ter pelo menos 18 anos."})

        return data


class DisciplinaSerializer(serializers.ModelSerializer):
    professor_nome = serializers.ReadOnlyField(source='Professor_responsavel.Nome')

    class Meta:
        model = Disciplina
        fields = ['id', 'Nome', 'Curso', 'Carga_Horaria', 'Descricao', 'Professor_responsavel', 'professor_nome']


class AmbienteSerializer(serializers.ModelSerializer):
    sala_numero = serializers.ReadOnlyField(source='Sala_reservada.numero')
    professor_nome = serializers.ReadOnlyField(source='Professor_responsavel.Nome')
    disciplina_nome = serializers.ReadOnlyField(source='Disciplina_professor.Nome')

    class Meta:
        model = Ambiente
        fields = [
            'id', 'Data_inicio', 'Data_termino', 'Periodo',
            'Sala_reservada', 'Disciplina_professor',
            'sala_numero', 'professor_nome', 'disciplina_nome'
        ]


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['id', 'numero']

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['tipo'] = user.Usuario
        token['nome'] = user.Nome
        return token