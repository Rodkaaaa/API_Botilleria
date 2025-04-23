from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repository.producto_repository import  create_producto, get_productos
from app.conection.database import get_db

router = APIRouter()
# Endpoint para crear un producto
@router.post("/productos/")
def add_producto(nombre: str, precio: float, cantidad: int, barcode: str, db: Session = Depends(get_db)):
    return create_producto(db, nombre, precio, cantidad, barcode)

# Endpoint para obtener todos los productos
@router.get("/productos/")
def list_productos(db: Session = Depends(get_db)):
    return get_productos(db)
