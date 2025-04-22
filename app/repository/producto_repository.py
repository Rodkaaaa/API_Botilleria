from sqlalchemy.orm import Session
from app.models.productos_model import Producto

def create_producto(db: Session, nombre: str, precio: float, stock: int):
    nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def get_productos(db: Session):
    return db.query(Producto).all()
