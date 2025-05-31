from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from extensions import Base

class Turno(Base):
    __tablename__ = 'turnos'

    id = Column(Integer, primary_key=True)
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'))
    dia_1 = Column(Boolean, default=False)
    dia_2 = Column(Boolean, default=False)
    noite_1 = Column(Boolean, default=False)
    noite_2 = Column(Boolean, default=False)
    local = Column(String)  # UH ou UCCI
