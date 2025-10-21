from django.shortcuts import render

def index(request):
    return render(request, 'buteco/index.html')

def mudarsenha(request):
    return render(request, 'buteco/mudarsenha.html')