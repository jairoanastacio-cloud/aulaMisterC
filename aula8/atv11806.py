from flask import Flask

app = Flask(__name__)
# Define uma rota ( endereco ) para a raiz "/"
@app.route("/jai")
def inicio():
    return "Jairo Marques Anastacio"
# Roda o servidor
if __name__ == "__main__":
    app.run(debug=True)