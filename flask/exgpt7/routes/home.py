from flask import Flask, request, render_template, Blueprint


home_route = Blueprint('home', __name__)

@home_route.route('/')
def index():
    return render_template('index.html')