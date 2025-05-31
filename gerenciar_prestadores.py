from sqlalchemy.orm import Session
from extensions import SessionLocal
from models import Funcionario, Turno

def gerenciar_prestadores():
    st.subheader("Buscar prestador por nome")

    nome_busca = st.text_input("Nome do prestador")

    if nome_busca:
        db: Session = SessionLocal()
        prestador = db.query(Funcionario).filter(Funcionario.nome.ilike(f"%{nome_busca}%")).first()

        if prestador:
            st.markdown("### Dados do Prestador")
            st.write(f"**Nome:** {prestador.nome}")
            st.write(f"**Matrícula:** {prestador.id}")
            st.write(f"**COREN:** {prestador.coren}")
            st.write(f"**Cargo:** {prestador.cargo}")
            st.write(f"**Tipo de vínculo:** {prestador.tipo_vinculo}")
            st.write(f"**Data de admissão:** {prestador.data_admissao}")

            st.markdown("---")
            st.markdown("### Plantões e Local")

            dia_1 = st.checkbox("Dia 1")
            dia_2 = st.checkbox("Dia 2")
            noite_1 = st.checkbox("Noite 1")
            noite_2 = st.checkbox("Noite 2")

            local = st.selectbox("Local", ["", "UH", "UCCI"])

            if st.button("Salvar"):
                turno = Turno(
                    funcionario_id=prestador.id,
                    dia_1=dia_1,
                    dia_2=dia_2,
                    noite_1=noite_1,
                    noite_2=noite_2,
                    local=local
                )
                db.add(turno)
                db.commit()
                st.success("Plantão salvo com sucesso.")
            db.close()

        else:
            st.warning("Prestador não encontrado.")
