from flask import Flask, render_template

app = Flask(__name__)

@app.route('/status/<nome>/<ativo>')
def status(nome, ativo):
    ativo = True if ativo == "1" else False
    return render_template('index.html',nome=nome, ativo=ativo)



app.run(debug=True)