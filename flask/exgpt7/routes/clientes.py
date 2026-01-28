from flask import Flask, request, render_template, Blueprint
from database.usuarios import usuarios
cliente_route = Blueprint('clientes', __name__)

@cliente_route.route('/signup', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if " " in usuario or " " in senha:
            return render_template("espaco.html")
        if usuario == "" or senha == "":
            return "Preencha ambos os campos!"
        elif usuario in usuarios:
            return "Usuário já cadastrado!!"
        else:
            usuarios[usuario] = senha


    return render_template('signup.html')

@cliente_route.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == "" or senha == "":
            return "Preencha ambos os campos!"
        elif usuario in usuarios and usuarios[usuario] == senha:
            return render_template("logged.html")
        elif (usuario,senha) not in usuarios:
            return "Usuário não cadastrado"
        



    return render_template('login.html')