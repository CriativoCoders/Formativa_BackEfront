# Importamos os módulos necessários do Django
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Definimos um modelo de usuário personalizado chamado ProfessorGestor
# que herda de AbstractUser, que já vem com campos como email e senha
class ProfessorGestor(AbstractUser):
    # Campo auto-incrementado que serve como identificador único
    Numero_indentificacao = models.AutoField(primary_key=True)
    
    # Campo para armazenar o nome do professor ou gestor
    Nome = models.CharField(max_length=200)
    
    # Campo para armazenar o telefone do professor ou gestor
    Telefone = models.CharField(max_length=100)
    
    # Campo para armazenar a data de nascimento do professor ou gestor
    Data_de_Nascimento = models.DateField(blank=True, null=True)
    
    # Campo para armazenar a data de contratação do professor ou gestor
    Data_de_contratacao = models.DateField(blank=True, null=True)
    
    # Campo para definir o tipo de usuário (Professor ou Gestor)
    Usuario = models.CharField(max_length=9, choices=(
        ('Professor','Professor'),
        ('Gestor','Gestor')
    ))

    # Campo que define se o usuário é staff ou não
    is_staff = models.BooleanField(default=True)  
    
    # Método que retorna uma string que representa o objeto
    def __str__(self):
        # Aqui eu mudei para usar o Numero_indentificacao em vez de NI
        return f"{self.Nome} - Numero_identificacao: {self.Numero_indentificacao}"


#Disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100, blank=True, null=True)
    carga_horaria = models.PositiveIntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    Professor_responsavel = models.ForeignKey(ProfessorGestor,on_delete=models.CASCADE, limit_choices_to={'Usuario':'Professor'},default=1,blank=True, null=True)

    def __str__(self):
        return self.nome


#Ambiente
class Ambiente(models.Model):
    # Campo para armazenar a data de início do ambiente
    Data_inicio = models.DateField(blank=True, null=True)
    # Campo para armazenar a data de término do ambiente
    Data_termino = models.DateField(blank=True, null=True)
    # Campo para definir o período do ambiente (Manhã, Tarde ou Noite)
    Periodo = models.CharField(max_length=10,choices=(
        ('M','Manhã'),
        ('T','Tarde'),
        ('N','Noite')
    ))
    # Campo que define a sala reservada para o ambiente
    Sala_reservada = models.ForeignKey('Sala', on_delete=models.CASCADE)
    
    # Campo que define o professor responsável pelo ambiente
    Professor_responsavel = models.ForeignKey(ProfessorGestor,on_delete=models.CASCADE, limit_choices_to={'Usuario':'Professor'})
    
    # Campo que define a disciplina do professor no ambiente
    Disciplina_professor = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)


# Sala
class Sala(models.Model):
    numero = models.PositiveBigIntegerField()

    def __str__(self):
        return f"sala {self.numero}"