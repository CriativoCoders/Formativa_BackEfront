from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ProfessorGestor  # Import the ProfessorGestor model

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('novo campo',{"fields":("Usuario",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Cargo",{'fields':('Usuario',)}),
    )

admin.site.register(ProfessorGestor, UsuarioAdmin)  # Pass the model class