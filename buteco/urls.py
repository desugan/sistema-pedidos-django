from .views import index, mudarsenha
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('mudarsenha/', mudarsenha, name='mudarsenha')
]