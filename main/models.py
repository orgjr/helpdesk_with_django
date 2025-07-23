from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuários: Herdando do AbstractUser para permitir futura integração com AD ou SSO
class Usuario(AbstractUser):
    departamento = models.CharField(max_length=100, blank=True, null=True)
    is_operador = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username


class Chamado(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em andamento'),
        ('fechado', 'Fechado'),
        ('negado', 'Negado'),
    ]

    SITUACAO_CHOICES = [
        ('resolvido', 'Resolvido'),
        ('nao_resolvido', 'Não resolvido'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chamados')
    motivo_categoria = models.CharField(max_length=255)
    descricao = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='nao_resolvido')
    data_fechamento = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.motivo_categoria}"


class Resposta(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name='respostas')
    operador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'is_operador': True})
    conclusao = models.TextField()
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resposta {self.id} para Chamado {self.chamado.id}"