from sqlalchemy.orm import Session
from app.models.usuarios_model import Usuario, UsuarioCreate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(
        nombre_usuario=usuario.nombre,
        rol=usuario.correo,
        contrasena=usuario.contrasena  # En producción, encriptar
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()
