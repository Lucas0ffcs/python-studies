from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    usuarios = [
        {"nome":"Lucas","ativo":1},
        {"nome": "Julia", "ativo": 0},
        {"nome": "Monkey", "ativo": 1}
    ]


@app.route('/status/<nome>/<ativo>')
def status(nome, ativo):
    ativo = True if ativo == "1" else False
    return render_template('index.html',nome=nome, ativo=ativo)



app.run(debug = True)