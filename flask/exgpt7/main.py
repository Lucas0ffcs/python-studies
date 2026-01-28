from flask import Flask, request, render_template
from routes.clientes import cliente_route
from routes.home import home_route



app = Flask(__name__)

app.register_blueprint(home_route)

app.register_blueprint(cliente_route, url_prefix='/clientes')

app.run(debug=True)