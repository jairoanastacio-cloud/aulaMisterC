from flask import Flask , jsonify
app = Flask(__name__)

produtos = [
{"id":1, "nome": "bola", "preco": 18.5},
{"id":2, "nome": "mouse", "preco": 16.0},
{"id":3, "nome": "bolsa", "preco": 59.2},
{"id":4, "nome": "chinelo", "preco": 15.5}
]

@app.route("/produtoss")
def listar_produtos():
    return jsonify(produtos)
 
if __name__ == "__main__":
    app.run(debug=True)