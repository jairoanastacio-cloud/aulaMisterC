from flask import Flask , jsonify
app = Flask(__name__)
@app.route("/produto")
def aluno():

    dados = {
            "id": 1,
            "nome": "Frigideira",
            "preco": 36.0,
            "dispo": True
            }
    return jsonify(dados)
if __name__ == "__main__":
    app.run(debug=True)
{
"dispo":True ,
"id": 1,
"nome": "Frigideira",
"preco": 36.0
}