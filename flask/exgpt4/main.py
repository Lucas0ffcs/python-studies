from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista = [
        {"usuario":"Lucas", "ativo":'1'},
        {"usuario":"Julia", "ativo":'0'},
        {"usuario":"Monkey", "ativo":'1'}
    ]


    return render_template('home.html', lista=lista)

@app.route('/status/<nome>/<ativo>')
def status(nome, ativo):
    ativo = True if ativo == '1' else False

    return render_template('status.html', nome=nome,ativo=ativo)




app.run(debug = True)