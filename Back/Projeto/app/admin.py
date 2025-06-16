from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ProfessorGestor, Disciplina, Ambiente, Sala

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('novo campo',{"fields":("Usuario",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets +  (
        ("Cargo",{'fields':('Usuario',)}),
    )

admin.site.register(ProfessorGestor, UsuarioAdmin)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome", 
        "curso", 
        "carga_horaria", 
        "descricao", 
        "Professor_responsavel",
        )

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "Data_inicio", 
        "Data_termino", 
        "Periodo", 
        "Sala_reservada", 
        "Professor_responsavel", 
        "Disciplina_professor",
        )

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "numero", 
        )