from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.usuarios_model import UsuarioCreate, UsuarioResponse
from app.repository import usuario_repository
from app.conection.database import get_db
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_repository.crear_usuario(db, usuario)

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return usuario_repository.obtener_usuarios(db)
