from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/thae")
def thae():
    return "Hello my name is thae thae.Welcome to my page."
