from sqlalchemy import Column, Integer, String, Float
from app.conection.database import Base
# Modelo Botilleria
class Botilleria(Base):
    __tablename__ = "botillerias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    dueño = Column(String, nullable=False)
    rut_empresa = Column(String, unique=True, nullable=False)
    direccion = Column(String, nullable=False)
    horario_inicio = Column(String, nullable=False)
    horario_termino = Column(String, nullable=False)