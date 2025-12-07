from pessoa import Pessoa
import sqlite3

class BancoDeDados:
    # Conectar ao banco de dados (ou criar um se não existir)
    conexao = sqlite3.connect('testedb.db', check_same_thread=False)
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()   
    
    # select * from pessoa
    def retornaTodasAsPessoas(self):
        sql = 'SELECT * FROM usuarios'
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()        
        return resultados  
        
    def retornaUltimoCadastrado(self):
        sql = 'SELECT * FROM usuarios'
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()        
        return resultados[-1]
    
    # select * from pessoa where id = id fornecido
    def retornaUmaPessoa(self, id):
        sql = f'SELECT * FROM usuarios WHERE id={id}'
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        if len(resultados) == 0:
            return "Nao encontrado"      
        return resultados[0]  

    # insert into pessoa
    def inserePessoa(self, id, nome, idade):
        self.cursor.execute('''
            INSERT INTO usuarios (nome, idade)
            VALUES (?, ?)
            ''', (nome, idade))
        
        self.conexao.commit()
        return self.retornaUltimoCadastrado()
    
    # delete * from pessoa where id = id fornecido
    def removePessoa(self, id):
        sql = f'DELETE FROM usuarios WHERE id={id}'
        self.cursor.execute(sql) 
        self.conexao.commit()    
        
    # update set ...
    def alterarPessoa(self, id, nome, idade):
        self.cursor.execute('''
            UPDATE usuarios SET nome=?, idade=?
            WHERE id=?
            ''', (nome, idade, id))        
        self.conexao.commit()
        return 
        
        

