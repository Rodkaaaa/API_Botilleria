from sqlalchemy import Column, Integer, String, Float
from app.conection.database import Base

# Modelo Producto
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    cantidad = Column(Integer)
    barcode = Column(String)