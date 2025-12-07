from pessoa import Pessoa

class BancoDeDados:
    
    tabelaPessoa = {}
    pessoa = Pessoa(1, "Maria", 25)
    tabelaPessoa[1] = pessoa     
    pessoa2 = Pessoa(2, "Marcos", 16) 
    tabelaPessoa[2] = pessoa2     
    pessoa3 = Pessoa(3, "Natalia", 28)
    tabelaPessoa[3] = pessoa3      
    pessoa4 = Pessoa(4, "Magda", 70) 
    tabelaPessoa[4] = pessoa4   
    
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
        
        

