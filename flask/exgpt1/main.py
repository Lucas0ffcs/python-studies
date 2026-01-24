from flask import Flask, Blueprint, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "home"

@app.route('/ola/<nome>')
def ola(nome):
    return render_template('index.html',nome=nome)



app.run(debug=True)