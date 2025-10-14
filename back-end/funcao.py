from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL          
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def inserir_filme(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_filme():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar listar filmes {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_filme(id_filme, nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET avaliacao = %s WHERE id = %s", 
                (nova_avaliacao, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar o filme {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_filmes(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filmes WHERE id = %s", 
                (id_filme,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar o filme {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes ORDER BY id = %s", (id_filme,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao tentar buscar filme {erro}")
        finally:
            cursor.close()
            conexao.close()