import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute(
    "UPDATE produtos SET nome = ?, preco = ? WHERE id = ?",
    ("Chapéu", 56.0, 2)
)

conexao.commit()
conexao.close()