from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Chamado, Usuario
from .forms import ChamadoForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home' if (getattr(request.user, 'is_operador', False))
                        else 'home_all')

    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)

            if getattr(user, 'is_operador', False):
                return redirect('home')
            return redirect('home_all')
    else:
        form = AuthenticationForm(request)

    return render(request, 'main/login.html', {'form': form, 'next': next_url})

@login_required
def home_all(request):
    return render(request, 'main/home.html', { 
        'usuario': request.user,
        'page': 'home_all'
    })

@login_required
def home(request):
    chamados_abertos = Chamado.objects.filter(status='aberto').order_by('-data_abertura')
    return render(request, 'main/home.html', { 
        'chamados_abertos': chamados_abertos,
        'usuario': request.user
    })

@login_required
def meus_chamados(request):
    chamados_usuarios = Chamado.objects.filter(usuario=request.user).order_by('-data_abertura')
    return render(request, "main/home.html", {
        'usuario': request.user,
        'chamados_usuarios': chamados_usuarios,
        'page': 'meus_chamados'  # controle de exibição no template
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