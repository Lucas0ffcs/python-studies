#main.py
from flask import Flask, render_template, request


app = Flask(__name__)

usuarios = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=["GET","POST"])
def signup():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if (usuario,senha) not in usuarios.items():
            usuarios[usuario] = senha
        else:
            return render_template('signup.html',jacadastrado="Usuário já cadastrado!",printer = usuarios)

        
    
        return render_template("cadastrado.html",printer = usuarios)

    return render_template("signup.html", printer = usuarios)   



@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if (usuario,senha) in usuarios.items():
            return render_template('logado.html')
        else:
            return render_template('login.html',negado="Usuário ou senha inválidos!!!")

    return render_template('login.html')


app.run(debug = True)