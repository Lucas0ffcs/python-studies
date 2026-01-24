from flask import Flask, request, render_template

usuarios = {}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == "" or senha == "":
            return "Preencha ambos os campos!"
        elif usuario in usuarios:
            return "Usuário já cadastrado!!"
        else:
            usuarios[usuario] = senha


    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')



app.run(debug=True)