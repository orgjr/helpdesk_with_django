from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Chamado, Resposta


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "departamento", "is_operador", "is_admin", "is_staff")
    list_filter = ("is_operador", "is_admin", "departamento", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("departamento", "is_operador", "is_admin")}),
    )


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "motivo_categoria", "status", "situacao", "data_abertura", "data_fechamento")
    list_filter = ("status", "situacao", "motivo_categoria", "data_abertura")
    search_fields = ("descricao", "usuario__username", "usuario__email")
    date_hierarchy = "data_abertura"
    readonly_fields = ("data_abertura", "updated_at")


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ("id", "chamado", "operador", "data_resposta")
    list_filter = ("data_resposta", "operador")
    search_fields = ("conclusao", "chamado__descricao", "operador__username")
    date_hierarchy = "data_resposta"