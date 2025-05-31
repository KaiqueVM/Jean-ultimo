from models import Funcionario
from datetime import date

def adicionar_prestador():
    with st.form("form_adicionar_prestador"):
        nome = st.text_input("Nome completo")
        mat = st.text_input("Matrícula (MAT)")
        coren = st.text_input("COREN")
        cargo = st.text_input("Cargo")
        data_admissao = st.date_input("Data de admissão", value=date.today())

        tipo_vinculo = st.selectbox(
            "Tipo de vínculo",
            ["AJ - PROGRAMA ANJO", "FT - EFETIVADO"]
        )

        salvar = st.form_submit_button("Salvar")

    if salvar:
        if not nome or not mat or not coren or not cargo:
            st.warning("Por favor, preencha todos os campos obrigatórios.")
            return

        existente = Funcionario.get_funcionario_por_id(mat)
        if existente:
            st.error("Já existe um prestador com essa matrícula.")
            return

        novo = Funcionario(
            id=mat,
            nome=nome,
            coren=coren,
            cargo=cargo,
            tipo_vinculo=tipo_vinculo,
            data_admissao=data_admissao,
            gerente=False  # prestadores não são gerentes
        )

        novo.save()

        st.success("Prestador cadastrado com sucesso!")
        st.rerun()
