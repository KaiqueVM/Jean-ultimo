import streamlit as st
from models import Funcionario  # seu modelo já adaptado
from datetime import date

# Inicializa o estado da sessão
def init_session():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False
        st.session_state["usuario"] = None
        st.session_state["pagina"] = "login"

# Tela de login
def login_screen():
    st.title("Pequeno Cotolengo - Login")

    coren = st.text_input("Corém")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        funcionario = Funcionario.get_funcionario_por_id(coren)

        if funcionario and funcionario.checa_senha(senha):
            if funcionario.cargo.lower() in ["gerente", "supervisor"]:
                st.session_state["autenticado"] = True
                st.session_state["usuario"] = {
                    "id": funcionario.id,
                    "nome": funcionario.nome,
                    "coren": funcionario.coren,
                    "cargo": funcionario.cargo,
                    "gerente": funcionario.gerente
                }
                st.success(f"Bem-vindo(a), {funcionario.nome}!")
            else:
                st.error("Apenas gerente ou supervisor têm acesso.")
        else:
            st.error("Corém ou senha inválidos.")

# Menu principal após login
def main_menu():
    st.sidebar.title("Menu")

    pagina = st.sidebar.radio(
        "Selecione uma opção:",
        ["Adicionar prestador", "Gerenciar prestadores", "Visualização geral"]
    )

    st.session_state["pagina"] = pagina

    if pagina == "Adicionar prestador":
        st.header("Adicionar novo prestador de serviço")
        adicionar_prestador()
    elif pagina == "Gerenciar prestadores":
        st.header("Gerenciar pessoas já cadastradas")
        gerenciar_prestadores()
    elif pagina == "Visualização geral":
        st.header("Visualização geral dos plantões")
        visualizacao_geral()
    
# Botão de logout
def logout_button():
    if st.sidebar.button("Sair"):
        st.session_state["autenticado"] = False
        st.session_state["usuario"] = None
        st.session_state["pagina"] = "login"
        st.experimental_rerun()

# Código principal
def main():
    st.set_page_config(page_title="Sistema Cotolengo", layout="wide")
    init_session()

    if not st.session_state["autenticado"]:
        login_screen()
    else:
        logout_button()
        main_menu()

if __name__ == "__main__":
    main()
