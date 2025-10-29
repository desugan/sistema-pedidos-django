from .views import index, mudarsenha, pedido, tela_login
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('login/', tela_login, name='login'),
    path('mudarsenha/', mudarsenha, name='mudarsenha'),
    path('pedido/', pedido, name='pedido'),
]