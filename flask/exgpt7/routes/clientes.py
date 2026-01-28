from flask import Flask, request, render_template, Blueprint
from database.connection import usuarios
from database.usuarios import addUser, logUser

cliente_route = Blueprint('clientes', __name__)

@cliente_route.route('/signup', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        email = request.form.get("email")
        senha = request.form.get("senha")



        ##NO TERCEIRO IF EU PRECISO MUDAR 'USUARIO IN USUARIO' PARA 'EMAIL IN EMAILS'
        if " " in usuario or " " in senha or " " in email:
            return render_template("espaco.html")
        if usuario == "" or senha == "" or email == "":
            return "Preencha ambos os campos!"
        #elif usuario in usuarios:
         #   return "Usuário já cadastrado!!"
        else:
            addUser(usuario, email, senha)

    return render_template('signup.html')
@cliente_route.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        ##ADICIONAR USUARIOEMAIL
        usuarioemail = request.form.get("usuarioemail")
        senha = str(request.form.get("senha"))

        return logUser(usuarioemail, senha)


    return render_template('login.html')