from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=["GET","POST"])
def signup():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form['senha']
    
    return render_template('index.html', usuario = usuario, senha=senha)



@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


app.run(debug = True)