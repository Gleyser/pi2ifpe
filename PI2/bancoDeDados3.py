from pessoa import Pessoa
import sqlite3

class BancoDeDados:
    
    # Conectar ao banco de dados (ou criar um se não existir)
    conexao = sqlite3.connect('testedb.db', check_same_thread=False)

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()
    
    # select * from pessoa
    def retornaTodasAsPessoas(self):
        return self.tabelaPessoa   
    
    # select * from pessoa where id = id fornecido
    def retornaUmaPessoa(self, id):
        pessoa = self.tabelaPessoa.get(id)
        return pessoa

    # insert into pessoa
    def inserePessoa(self, id, nome, idade):
        novaPessoa = Pessoa(id, nome, idade)
        self.tabelaPessoa[id] = novaPessoa
        return novaPessoa
    
    # delete * from pessoa where id = id fornecido
    def removePessoa(self, id):
        if(id in self.tabelaPessoa):
            self.tabelaPessoa.pop(id)
            return True
        return False            
        
    # update set ...
    def alterarPessoa(self, id, nome, idade):
        Pessoa = self.tabelaPessoa.get(id)
        Pessoa.nome = nome
        Pessoa.idade = idade
        return Pessoa
        
        

