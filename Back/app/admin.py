from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# definindo a minha classe usuario admin, e adionando novos campos etc.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('novo campo',{"fields":("usuario",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Cargo",{'fields':('usuario',)}),
    )

admin.site.register(ProfessorGestor,UsuarioAdmin)


