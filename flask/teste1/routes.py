from main import app


@app.route("/")
def homepage():
    return "Meu site no Flask"

@app.route("/blog")
def blog():
    return "Bem vindo ao blog"