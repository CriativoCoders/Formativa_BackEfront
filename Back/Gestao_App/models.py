from django.db import models
from django.contrib.auth.models import AbstractUser

class Professor(AbstractUser):
    indentificacao = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)

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

