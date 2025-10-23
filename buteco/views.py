from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def index(request):
    if request.user.is_authenticated:
        return redirect('pedido')
    return redirect('login')

def login(request):
    return render(request, 'buteco/login.html')

def mudarsenha(request):
    return render(request, 'buteco/mudarsenha.html')

def pedido(request):
    return render(request, 'buteco/pedido.html')


