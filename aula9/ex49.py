from flask import Flask , jsonify
app = Flask(__name__)

produtoz = [
{"id":1, "nome": "bola", "preco": 18.5, "disponivel": True},
{"id":2, "nome": "mouse", "preco": 16.0, "disponivel": False},
{"id":3, "nome": "bolsa", "preco": 59.2, "disponivel": True},
{"id":4, "nome": "chinelo", "preco": 15.5, "disponivel": False}
]

@app.route("/produtoz")
def listar_produtos():
    return jsonify(produtoz)

@app.route("/produtoz/dispo")
def listar_prod_dispo():
    prodf = []
    for produto in produtoz:
        if produto["disponivel"]:
            prodf.append(produto)
    return jsonify(prodf)
    
if __name__ == "__main__":
    app.run(debug=True)