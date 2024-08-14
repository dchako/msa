from sqlalchemy import Column, Integer, String
from .database import Base

class CalculoEscanos(Base):
    __tablename__ = "calculo_escanos"

    id = Column(Integer, primary_key=True, index=True)
    escaños = Column(Integer, index=True)
    votos = Column(String, index=True)
    resultado = Column(String)
