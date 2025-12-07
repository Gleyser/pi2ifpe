# Importando as bibliotecas: fastapi e basemodel
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4
from bancoDeDados import BancoDeDados
from fastapi.middleware.cors import CORSMiddleware

# --- Configurações da API (Metadados Globais) ---
tags_metadata = [
    {
        "name": "Produtos",
        "description": "Gerenciamento completo do catálogo de produtos. Permite **criar**, **listar**, **atualizar** e **deletar** itens.",
    }
]

# --- Modelo de Dados 
class Produto(BaseModel):
    id: Optional[str] = Field(
        None, 
        description="Identificador único do produto (UUID). Gerado automaticamente na criação.",
        example="a1b2c3d4-e5f6-7890-1234-56789abcdef0"
    )
    nome: str = Field(
        ..., 
        title="Nome do Produto", 
        description="O nome comercial do produto. Deve ter entre 3 e 100 caracteres.", 
        min_length=3, 
        max_length=100,
        example="Notebook Gamer Dell"
    )
    preco: float = Field(
        ..., 
        gt=0, 
        description="Preço unitário do produto. Deve ser maior que zero.",
        example=4500.00
    )   

    class Config:
        schema_extra = {
            "example": {
                "nome": "Notebook Gamer Dell",
                "preco": 4500.00                
            }
        }

app = FastAPI(
    title="API de Gestão de Produtos",
    description="""
    API de exemplo para IFPE - Programação para Internet II""",
    version="1.0.0",   
    openapi_tags=tags_metadata
)

origins = ["*"] # Em produção, troque "*" pelo domínio do seu site

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Banco de Dados Simulado (Em memória) ---
banco: List[Produto] = []

# --- 1. POST: Criar um Produto ---
@app.post(
    "/produtos", 
    response_model=Produto, 
    status_code=status.HTTP_201_CREATED,
    tags=["Produtos"],
    summary="Criar um novo produto",
    description="Adiciona um novo produto ao banco de dados. O **ID** será gerado automaticamente."
)
def create_product(product: Produto):
    product.id = str(uuid4())
    banco.append(product)
    return product

# --- 2. GET: Listar todos os Produtos ---
@app.get(
    "/produtos", 
    response_model=List[Produto],
    tags=["Produtos"],
    summary="Listar todos os produtos",
    description="Retorna uma lista contendo todos os produtos cadastrados no sistema."
)
def get_products():
    return banco

# --- 2.1 GET: Buscar um Produto por ID ---
@app.get(
    "/produtos/{product_id}", 
    response_model=Produto,
    tags=["Produtos"],
    summary="Obter produto por ID",
    description="Busca os detalhes de um produto específico baseado no seu UUID.",
    responses={404: {"description": "Produto não encontrado"}}
)
def get_product(product_id: str):
    # Procura o produto na lista
    produto = next((p for p in banco if p.id == product_id), None)
    
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto

# --- 3. PUT: Atualizar um Produto ---
@app.put(
    "/produtos/{product_id}", 
    response_model=Produto,
    tags=["Produtos"],
    summary="Atualizar produto",
    description="Atualiza os dados de um produto existente. O ID não pode ser alterado."
)
def update_product(product_id: str, updated_product: Produto):
    # Encontra o índice do produto na lista
    index = next((i for i, p in enumerate(banco) if p.id == product_id), None)
    
    if index is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Mantém o ID original e atualiza os dados
    updated_product.id = product_id
    banco[index] = updated_product
    
    return updated_product

# --- 4. DELETE: Deletar um Produto ---
@app.delete(
    "/produtos/{product_id}", 
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Produtos"],
    summary="Deletar produto",
    description="Remove permanentemente um produto do banco de dados."
)
def delete_product(product_id: str):
    index = next((i for i, p in enumerate(banco) if p.id == product_id), None)
    
    if index is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    banco.pop(index)
    return # Retorna vazio (204 No Content)




