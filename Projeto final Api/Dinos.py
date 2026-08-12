from flask import Flask, jsonify, request
import sqlite3

dinos = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("dino.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabelas():
    conexao = conectar()

    conexao.execute("""
            create table if not exists era(
                id integer primary key autoincrement,
                periodo text
                )       
             """)

    conexao.execute("""
                create table if not exists dinossauro(
                    id integer primary key autoincrement,
                    nome text,
                    ordem text,
                    local text,
                    era_id integer,
                    foreign key (era_id) references era(id)
                    )       
                 """)

    conexao.commit()
    conexao.close()

@dinos.route("/eras", methods=["GET"])
def listar_eras():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM era")
    result = [dict(row) for row in cursor.fetchall()]
    conexao.close()
    return jsonify(result)

@dinos.route("/eras", methods=["POST"])
def criar_tutor():
    dados = request.get_json()

    if "periodo" not in dados or dados ["periodo"] == "":
        return jsonify({"erro": "o campo nome eh obrigatorio"}), 400
    
    conexao = conectar()
    cursor = conexao.execute(
    "INSERT INTO era (periodo) VALUES (?)",
    (dados ["periodo"])
     )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    
    return jsonify({"id": novo_id, **dados}), 201

@dinos.route("/eras/<int:eras_id>", methods=["GET"])
def buscar_tutor(tutor_id):
        conexao = conectar()
        cursor = conexao.execute("SELECT FROM tutor WHERE id cursor = ?", (tutor_id,))
        linha = cursor.fetchone()
        conexao.close()

        if linha is None:
         return jsonify({"erro": "Era não encontrada"}), 404
        
        return jsonify(dict(linha))

if __name__ == "__main__":
    dinos.run(debug=True, port=5001)