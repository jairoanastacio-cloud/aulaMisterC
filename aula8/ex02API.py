from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Bem Vindo"
@app.route("/curso")
def sobre():
    return "Desenvolvimento de Sistemas"
@app.route("/escola")
def aluno():
    return "CEEP Pedro Boaretto neto"
if __name__ == "__main__":
    app.run(debug=True)