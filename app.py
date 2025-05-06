import streamlit as st
import pandas as pd
from database import criar_tabela, adicionar_produto, listar_produtos

# Inicializa o banco de dados
criar_tabela()

# Configuração da página
st.set_page_config(page_title="Sistema de Estoque", layout="wide")
st.title("📦 Sistema de Estoque")

# ----------- Menu Lateral -----------
st.sidebar.title("📁 Menu")
pagina = st.sidebar.radio(
    "Navegar para:",
    ["➕ Adicionar Produto", "📋 Ver Estoque"]
)

# ----------- Página: Adicionar Produto -----------
if pagina == "➕ Adicionar Produto":
    st.header("➕ Adicionar Novo Produto")
    col1, col2, col3 = st.columns(3)

    with col1:
        nome = st.text_input("Nome do Produto")

    with col2:
        categoria = st.text_input("Categoria")

    with col3:
        quantidade = st.number_input("Quantidade", min_value=0, step=1)

    if st.button("Salvar Produto"):
        if nome != "":
            adicionar_produto(nome, categoria, quantidade)
            st.success("Produto adicionado com sucesso!")
        else:
            st.warning("O nome do produto é obrigatório.")

# ----------- Página: Ver Estoque -----------
elif pagina == "📋 Ver Estoque":
    st.header("📋 Estoque Atual")
    dados = listar_produtos()
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Categoria", "Quantidade"])
    st.dataframe(df, use_container_width=True)
