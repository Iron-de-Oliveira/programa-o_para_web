from flask import Flask; from flask import template

app = Flask(__name__)

@app.route("/")
def rota1():
    return("meu nome é iron")

@app.route("/rota2")
def rota2():
    return("meu nome é iron 2")

if __name__ == "__main__":
    app.run(debug=True)
