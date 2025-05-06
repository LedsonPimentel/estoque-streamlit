import streamlit as st
from database import criar_tabela, adicionar_produto, listar_produtos, atualizar_quantidade

st.set_page_config(page_title="Controle de Estoque", layout="centered")
criar_tabela()

st.title("📦 Sistema de Controle de Estoque")

# Menu lateral
pagina = st.sidebar.radio("Menu", ["➕ Adicionar Produto", "📋 Ver Estoque", "🔄 Atualizar Estoque"])

# ----------- Página: Adicionar Produto -----------
if pagina == "➕ Adicionar Produto":
    st.header("➕ Adicionar Novo Produto")

    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)

    if st.button("Adicionar"):
        if nome and quantidade >= 0:
            adicionar_produto(nome, categoria, quantidade)
            st.success(f"Produto '{nome}' adicionado com sucesso!")
        else:
            st.warning("Preencha todos os campos corretamente.")

# ----------- Página: Ver Estoque -----------
elif pagina == "📋 Ver Estoque":
    st.header("📋 Produtos em Estoque")

    produtos = listar_produtos()
    if produtos:
        st.table(produtos)
    else:
        st.info("Nenhum produto cadastrado ainda.")

# ----------- Página: Atualizar Estoque -----------
elif pagina == "🔄 Atualizar Estoque":
    st.header("🔄 Atualizar Quantidade em Estoque")

    produtos = listar_produtos()
    if produtos:
        opcoes = {f"{p[1]} (ID: {p[0]}) - {p[3]} un.": p for p in produtos}
        selecao = st.selectbox("Selecione um produto", list(opcoes.keys()))
        produto = opcoes[selecao]

        # Opção para adicionar ou subtrair
        operacao = st.radio("Escolha a operação", ("Adicionar", "Subtrair"))

        qtd_alterada = st.number_input(f"Quantidade a {operacao.lower()}", step=1)

        if st.button("Atualizar"):
            if operacao == "Adicionar":
                nova_qtd = produto[3] + qtd_alterada
            else:  # Subtrair
                nova_qtd = produto[3] - qtd_alterada

            if nova_qtd < 0:
                st.warning("A quantidade final não pode ser negativa.")
            else:
                atualizar_quantidade(produto[0], nova_qtd)
                st.success(f"Estoque atualizado com sucesso! Novo estoque: {nova_qtd} unidades.")
    else:
        st.info("Nenhum produto cadastrado ainda.")
