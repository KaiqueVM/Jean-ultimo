import pandas as pd
from extensions import SessionLocal
from models import Funcionario, Turno
from calendar import monthrange
from datetime import datetime

def visualizacao_geral():
    st.subheader("Visualização Geral dos Plantões")

    mes_atual = datetime.today().month
    ano_atual = datetime.today().year
    dias_no_mes = monthrange(ano_atual, mes_atual)[1]

    db = SessionLocal()
    funcionarios = db.query(Funcionario).all()
    turnos = db.query(Turno).all()

    # Prepara a tabela base
    data = []

    for f in funcionarios:
        linha = {
            "Nome": f.nome,
            "Matrícula": f.id,
            "Programa": f.tipo_vinculo
        }

        # Inicializa colunas para cada dia com string vazia
        for dia in range(1, dias_no_mes + 1):
            linha[str(dia)] = ""

        # Filtra turnos do funcionário
        turnos_do_func = [t for t in turnos if t.funcionario_id == f.id]

        for t in turnos_do_func:
            dias_turno = []
            if t.dia_1: dias_turno.append("D1")
            if t.dia_2: dias_turno.append("D2")
            if t.noite_1: dias_turno.append("N1")
            if t.noite_2: dias_turno.append("N2")

            texto_turno = ", ".join(dias_turno)
            texto_final = f"{texto_turno} - {t.local}" if texto_turno else ""

            # Aqui colocamos o turno no dia 1 apenas (ou podemos expandir)
            if texto_final:
                linha["1"] += texto_final  # Simples: tudo no dia 1 por enquanto

        data.append(linha)

    db.close()

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)
