import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL
)
""")

cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Carro", 15000.90))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Boné", 25.00))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Botina", 280.50))


conexao.commit()
conexao.close()

print("Produtos inseridos")