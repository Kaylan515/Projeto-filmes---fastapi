import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")
st.title("🎥 Gerenciador de filmes")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar filme"])

if menu == "Catalogo":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            st.dataframe(filmes)
    else:
        st.error("Erro ao acessar a API")

elif menu == "Adicionar filme":
    st.subheader("➕ Adicionar filmes")
    titulo = st.text_input("Título do Filme")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de Lançamento", min_value=1800, max_value=2100, step=1)
    avaliacao = st.number_input("Avaliação de (0 a 10)", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("Adicionar Filme"):
        dados = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionando com sucesso!")
        else:
            st.error("Erro ao adicionar o filme")

elif menu == "Atualizar filmes":
    st.subheader("Atualização de filmes")
    