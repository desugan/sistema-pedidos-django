from .views import index, mudarsenha, pedido, login
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('mudarsenha/', mudarsenha, name='mudarsenha'),
    path('pedido/', pedido, name='pedido')
]