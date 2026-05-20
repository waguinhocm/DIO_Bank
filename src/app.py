from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bemvindo/<usuario>/<int:idade>/<float:altura>')
def bem_vindo(usuario, idade, altura):
    return {
        "Usuario": usuario,
        "Idade": idade,
        "Altura": altura,
    }

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about/', methods=["GET","POST"])
def about():
    if request.method == "GET":
        return 'This is a GET'
    else:
        return 'This is a POST'

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('bem_vindo', usuario="Wagner", idade=45, altura=1.73))
    print(url_for('about', next='/'))
    print(url_for('projects'))