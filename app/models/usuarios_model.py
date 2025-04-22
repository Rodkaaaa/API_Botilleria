from sqlalchemy import Column, Integer, String
from app.conection.database import Base
from pydantic import BaseModel

# Modelo SQLAlchemy
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contrasena = Column(String, nullable=False)

# Modelo Pydantic para entrada/salida
class UsuarioCreate(BaseModel):
    nombre_usuario: str
    contrasena: str
    rol: str


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str

    class Config:
        from_attributes = True
