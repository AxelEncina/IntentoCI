from flask import Flask
var = "Hola Mundo";
var = "Hola Mundo";
var = "Hola Mundo";
var = "Hola Mundo";

app = Flask(__name__)

@app.route("/")

def index():
    return var

if __name__ == "__main__":
    app.run()

def index2():
    return