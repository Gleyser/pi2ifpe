import sqlite3

# Conectar ao banco de dados (ou criar um se não existir)
conexao = sqlite3.connect('testedb.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar uma tabela de exemplo
#cursor.execute('''
#CREATE TABLE IF NOT EXISTS usuarios (
 #   id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nome TEXT NOT NULL,
 #   idade INTEGER
#)
#''')

# Inserir dados de exemplo
#cursor.execute('''
#INSERT INTO usuarios (nome, idade)
#VALUES (?, ?)
#''', ('João', 30))

#cursor.execute('DELETE FROM usuarios')

# Confirmar a transação
#conexao.commit()

# Consultar dados
cursor.execute('SELECT * FROM usuarios')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

# Fechar a conexão
conexao.close()
