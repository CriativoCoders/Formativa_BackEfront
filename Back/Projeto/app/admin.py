from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ProfessorGestor, Disciplina, Ambiente, Sala# Import the ProfessorGestor model

# class UsuarioAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ('novo campo',{"fields":("Usuario",)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ("Cargo",{'fields':('Usuario',)}),
#     )

# admin.site.register(ProfessorGestor, UserAdmin)  # Pass the model class

@admin.register(ProfessorGestor)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {
            "fields": (
                "Numero_indentificacao",
                "Nome",
                "Telefone",
                "Data_de_Nascimento",
                "Data_de_contratacao",
                "Usuario",
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informações adicionais", {
            'fields': (
                "Numero_indentificaçao",
                "Nome",
                "Telefone",
                "Data_de_nascimento",
                "Data_de_contratação",
                "Usuario",
            )
        }),
    )

    list_display = (
        "Numero_indentificacao",
        "Nome",
        "Usuario",
        "Telefone",
        "Data_de_Nascimento",
        "Data_de_contratacao",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("Nome", "Usuario", "Telefone")
    list_filter = ("Usuario", "is_staff", "is_superuser")


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
        "Disiciplina_professor",
        )
    

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "nome", 
        "capacidade", 
        "tipo",
        )
    



# fazer novas mudanças