### serializers.py_pasta da aplicação futuras modificações...

```python
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
```

#

### views.py

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Professor, Disciplina, ReservaAmbiente
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaAmbienteSerializer

class ProfessorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

class ProfessorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            professor = Professor.objects.get(pk=pk)
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data)
        except Professor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProfessorUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            professor = Professor.objects.get(pk=pk)
            serializer = ProfessorSerializer(professor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Professor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProfessorDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            professor = Professor.objects.get(pk=pk)
            professor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Professor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Disciplinas
class DisciplinaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views para Reservas de Ambiente
class ReservaAmbienteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.tipo != Professor.GESTOR:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ReservaAmbienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaAmbienteListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.tipo == Professor.GESTOR:
            reservas = ReservaAmbiente.objects.all()
        else:
            reservas = ReservaAmbiente.objects.filter(professor_responsavel=request.user)
        serializer = ReservaAmbienteSerializer(reservas, many=True)
        return Response(serializer.data)

# Views adicionais para professores
class ProfessorDisciplinaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        disciplinas = Disciplina.objects.filter(professor_responsavel=request.user)
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

class ProfessorReservaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservas = ReservaAmbiente.objects.filter(professor_responsavel=request.user)
        serializer = ReservaAmbienteSerializer(reservas, many=True)
        return Response(serializer.data)
```

#

### urls.py
```python
from django.urls import path
from .views import (
    ProfessorView, ProfessorListView, ProfessorDetailView, ProfessorUpdateView, ProfessorDeleteView,
    DisciplinaView, ReservaAmbienteView, ReservaAmbienteListView,
    ProfessorDisciplinaView, ProfessorReservaView
)

urlpatterns = [
    # Professores
    path('professores/', ProfessorView.as_view(), name='criar_professor'),
    path('professores/lista/', ProfessorListView.as_view(), name='lista_professores'),
    path('professores/<int:pk>/', ProfessorDetailView.as_view(), name='detalhe_professor'),
    path('professores/<int:pk>/atualizar/', ProfessorUpdateView.as_view(), name='atualizar_professor'),
    path('professores/<int:pk>/excluir/', ProfessorDeleteView.as_view(), name='excluir_professor'),

    # Disciplinas
    path('disciplinas/', DisciplinaView.as_view(), name='criar_disciplina'),

    # Reservas de Ambiente
    path('reservas/', ReservaAmbienteView.as_view(), name='criar_reserva'),
    path('reservas/lista/', ReservaAmbienteListView.as_view(), name='lista_reservas'),

    # Views adicionais para professores
    path('professor/disciplinas/', ProfessorDisciplinaView.as_view(), name='disciplinas_professor'),
    path('professor/reservas/', ProfessorReservaView.as_view(), name='reservas_professor'),
]
```

#

### models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class Professor(AbstractUser):
    PROFESSOR = 'PROFESSOR'
    GESTOR = 'GESTOR'
    OUTRO = 'OUTRO'

    TIPOS = [
        (PROFESSOR, 'Professor'),
        (GESTOR, 'Gestor'),
        (OUTRO, 'Outro'),
    ]

    indentificacao = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=TIPOS, default=PROFESSOR)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100, blank=True, null=True)
    carga_horaria = models.PositiveIntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='disciplinas')

    def __str__(self):
        return self.nome

class ReservaAmbiente(models.Model):
    MANHA = 'Manhã'
    TARDE = 'Tarde'
    NOITE = 'Noite'
    PERIODOS = [
        (MANHA, 'Manhã'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    ]

    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    periodo = models.CharField(max_length=6, choices=PERIODOS)
    sala_reservada = models.CharField(max_length=50)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='reservas')
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.sala_reservada} - {self.periodo} de {self.data_inicio.strftime('%d/%m/%Y')}"
```