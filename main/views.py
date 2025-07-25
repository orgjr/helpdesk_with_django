from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Chamado
from .forms import ChamadoForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # ou para a página principal do sistema

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # ou redirecionar para a página inicial do sistema
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})


@login_required
def home(request):
    chamados_abertos = Chamado.objects.filter(status='aberto').order_by('-data_abertura')
    return render(request, 'main/home.html', { 
        'chamados_abertos': chamados_abertos,
        'usuario': request.user
    })

@login_required
def meus_chamados(request):
    return render(request, "main/home.html", {
        'usuario': request.user,
        'page': 'meus_chamados'  # você pode usar isso para controle de exibição no template
    })

@login_required
def novo_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.usuario = request.user
            chamado.save()
            return render(request, "main/home.html", {'page': 'chamados_criados', 'usuario': request.user})  # ou outra URL
    else:
        form = ChamadoForm()
    return render(request, "main/home.html", {'page': 'novo_chamado', 'form': form, 'usuario': request.user})

@login_required
def chamados_atribuidos(request):
    return render(request, "main/home.html", {
        'usuario': request.user,
        'page': 'chamados_atribuidos'
    })

@login_required
def painel_admin(request):
    return render(request, "main/home.html", {
        'usuario': request.user,
        'page': 'painel_admin'
    })

@login_required
def chamados_criados(request): 
    return render(request, "main/home.html", {
        'usuario': request.user,
        'page': 'painel_admin'
    })