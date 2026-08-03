import sqlite3
conexao = sqlite3.connect ("loja.db")
cursor = conexao.cursor ()

cursor.execute("DELETE FROM produtos WHERE id = ?" , (3 ,))

conexao.commit()
conexao.close()

if cursor.rowcount == 0:
    print("Nenhum produto com esse id foi encontrado")
else:
    print("Produto apagado com sucesso")