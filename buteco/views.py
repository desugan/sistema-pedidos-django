import os
from django.shortcuts import render, redirect
from django.contrib import messages
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


def index(request):
    if request.user.is_authenticated:
        return redirect('pedido')
    return redirect('login')


def login_view(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
    
        user = _consultaUsuario(usuario, senha)

        if user:
            return redirect('pedido')
        else:
            return render(request, 'login', {'error': 'Credenciais inválidas'})
    return render(request, 'login')


def tela_login(request):
    return render(request, 'buteco/login.html')

def mudarsenha(request):
    return render(request, 'buteco/mudarsenha.html')

def pedido(request):
    return render(request, 'buteco/pedido.html')


def _consultaUsuario(usuario, senha):

    conexao = None
    cursor = None
    try:

        conexao = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
        )

        cursor = conexao.cursor()

        query = """
            SELECT * FROM usuario
            WHERE usuario = %s AND senha = %s
            LIMIT 1
        """

        cursor.execute(query, (usuario, senha))

        return cursor.fetchall()

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados ou executar a query: {erro}")
        return False

    finally:
        # Garantir que o cursor e a conexão sejam fechados     
        if conexao:
            conexao.close()
