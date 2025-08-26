from .views import home_all, home, login_view, meus_chamados, novo_chamado, painel_admin, chamados_atribuidos, chamados_criados
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('home-all/', home_all, name='home_all'),
    path('meus-chamados/', meus_chamados, name='meus_chamados'),
    path('novo-chamado/', novo_chamado, name='novo_chamado'),
    path('painel-admin/', painel_admin, name='painel_admin'),
    path('chamados-criados/', chamados_criados, name='chamados_criados'),
    path('chamados-atribuídos/', chamados_atribuidos, name='chamados_atribuidos'),
    path('login', login_view, name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'),
]
