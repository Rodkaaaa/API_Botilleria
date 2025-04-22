from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repository.botilleria_repository import create_botilleria, get_botillerias
from app.conection.database import get_db

router = APIRouter()

# Endpoint para crear una botillería
@router.post("/post/botillerias/")
def add_botilleria(nombre: str, dueño: str, rut_empresa: str, direccion: str, horario_inicio: str, horario_termino: str, db: Session = Depends(get_db)):
    return create_botilleria(db, nombre, dueño, rut_empresa, direccion, horario_inicio, horario_termino)

# Endpoint para obtener todas las botillerías
@router.get("/get/botillerias/")
def list_botillerias(db: Session = Depends(get_db)):
    return get_botillerias(db)

