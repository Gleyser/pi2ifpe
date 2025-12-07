class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def setNome(self, novoNome):
        self.nome = novoNome

    def setIdade(self, novaIdade):
        self.idade = novaIdade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    
    def getId(self):
        return self.id 
    