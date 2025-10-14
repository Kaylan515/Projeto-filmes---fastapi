from fastapi import FastAPI
from funcao import listar_filme, deletar_filmes, criar_tabela, inserir_filme, atualizar_filme, buscar_filme

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
    return{"mensagem": "Bem vindo ao Gerenciador de Filmes"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = listar_filme()
    lista = []
    for filme in filmes:
        lista.append({ 
            "id": filme[0], 
            "titulo": filme[1], 
            "genero": filme[2], 
            "ano": filme[3], 
            "avaliacao": filme[4]})
    return {"filmes": lista}

@app.put("/filmes")
def atualizar_filmes(id_filme: int, nova_avaliacao: float):
    filme = atualizar_filme(id_filme)
    if filme:
        buscar_filme(id_filme, nova_avaliacao)
        return {"mensagem": "Filme atualizado ✔"}
    else:
        return{"erro": "Filme não atualizado"}