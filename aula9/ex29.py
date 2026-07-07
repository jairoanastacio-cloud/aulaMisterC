from flask import Flask , jsonify
app = Flask(__name__)

produtos = [
{"id":1, "nome": "bola", "preco": 18.5},
{"id":2, "nome": "mouse", "preco": 16.0},
{"id":3, "nome": "bolsa", "preco": 59.2},
{"id":4, "nome": "chinelo", "preco": 15.5}
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/<int:id>")
def buscar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)

    return jsonify({" erro ": "Produto nao encontrado"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)