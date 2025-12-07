from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from bancoDeDados2 import BancoDeDados

app = FastAPI()
banco = BancoDeDados()

class Pessoa(BaseModel):
    id: int
    nome: str
    idade: int


@app.get("/")
def inicio():
    return {"Olá, Maria!"}

@app.get("/pedrasdefogo")
def pedrasDeFogo():
    return {"Seja bem-vindo a Joao Pessoa"}

@app.get("/oi")
def oi():
    return "Oi, elisangela"

@app.get("/oisabido/{nome}")
def oisabido(nome:str):
    return f"Oi, {nome}"

@app.get("/aposentadoria/{idade}")
def aposentadoria(idade: int):
    if idade >= 65:
        return "Pode se aposentar"
    return "Não pode se aposentar"  

@app.get("/aposentadoria/{idade}/{sexo}")
def aposentadoria(idade: int, sexo: str):
    if idade >= 65 and sexo == "M":
        return "Pode se aposentar"
    elif idade >= 60 and sexo == "F":
        return "Pode se aposentar"
    return "Não pode se aposentar"

@app.get("/votar/{idade}")
def votar(idade:int):
    if idade >= 16:
        return "Pode votar"
    return "Não pode votar"

@app.get("/par/{numero}")
def par(numero:int):
    if numero%2 == 0:
        return "É par"
    return "É impar"

@app.get("/vogais/{palavra}")
def vogais(palavra:str):
    palavra = palavra.lower()
    vogais = ["a", "e", "i", "o", "u"]
    for vogal in vogais:
        palavra = palavra.replace(vogal, '*')
    return palavra

@app.get("/login/{email}/{senha}")
def login(email: str, senha: str):
    return "login feito com sucesso"

@app.post("/cadastrar/pessoa")
def cadastrarPessoa(pessoa: Pessoa):    
    return banco.inserePessoa(
        pessoa.id, pessoa.nome, pessoa.idade)

@app.get("/pessoas")
def recuperarPessoas():
    return banco.retornaTodasAsPessoas()

@app.get("/pessoas/{id}")
def recuperarUmaPessoa(id : int):
    return banco.retornaUmaPessoa(id)

@app.delete("/pessoas/{id}")
def deletarUmaPessoa(id: int):
    return banco.removePessoa(id)

@app.put("/pessoas")
def modificarUmaPessoa(pessoa: Pessoa):
    return banco.alterarPessoa(
        pessoa.id, pessoa.nome, pessoa.idade)




