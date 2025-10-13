from fastapi import FastAPI
from funcao import listar_filme, deletar_filmes, criar_tabela, inserir_filme, atualizar_filme

# Rodar o fastapi:
# python -m uvicorn api:app --reload

#Testar api FastAPI
# /docs > Documentação Swagger
# /redoc > Documentação redoc

#Iniciar o fastapi
app = FastAPI(title="Gerenciador de filmes")

#GET = Pegar / listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = deletar

# 127.0.0.1:8000
@app.get("/")
def home():
    return{"mensagem": "Quero café prof"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}