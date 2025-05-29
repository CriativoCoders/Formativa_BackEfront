from rest_framework import serializers
from .models import Professor, Disciplina, ReservaAmbiente

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'email', 'telefone', 'data_nascimento', 'data_contratacao', 'tipo']

class DisciplinaSerializer(serializers.ModelSerializer):
    professor_responsavel = ProfessorSerializer()

    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'curso', 'carga_horaria', 'descricao', 'professor_responsavel']

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    professor_responsavel = ProfessorSerializer()
    disciplina_associada = DisciplinaSerializer()

    class Meta:
        model = ReservaAmbiente
        fields = ['id', 'data_inicio', 'data_termino', 'periodo', 'sala_reservada', 'professor_responsavel', 'disciplina_associada']