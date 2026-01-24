from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista = [
        {"usuario":"Lucas", "ativo":True},
        {"usuario":"Julia", "ativo":False},
        {"usuario":"Monkey", "ativo":True}

    ]


    return render_template('home.html', lista=lista)

@app.route('/status/<nome>/<ativo>')
def status(nome, ativo):
    ativo = ativo == "1"

    return render_template('status.html', nome=nome,ativo=ativo)




app.run(debug = True)