# forms.py
from django import forms
from .models import Chamado

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['motivo_categoria', 'descricao']
        widgets = {
            'motivo_categoria': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ex: Problema no sistema...'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Descreva o problema detalhadamente...'
            }),
        }