from flask import Flask , jsonify
app = Flask(__name__)
@app.route("/produtos")
def aluno():

    dados = {"id": 1,"nome": "Frigideira","preco": 36.0,"dispo": True,
             "id": 2,"nome": "Bola","preco": 30.0,"dispo": True,
             "id": 3,"nome": "Geladeira","preco": 850.0,"dispo": True,
             "id": 4,"nome": "Bolsa","preco": 55.0,"dispo": True,
             
            }
    return jsonify(dados)
if __name__ == "__main__":
    app.run(debug=True)
{"dispo":True ,"id": 1,"nome": "Frigideira","preco": 36.0}
{"dispo":True ,"id": 2,"nome": "Bola","preco": 30.0}
{"dispo":True ,"id": 3,"nome": "Geladeira","preco": 850.0}
{"dispo":True ,"id": 4,"nome": "Bolsa","preco": 55.0}