from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/', methods=["GET","POST"])
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
    
        return f"Usuário: {usuario} Senha: {senha}"
    return "Página de login"


app.run(debug=True)