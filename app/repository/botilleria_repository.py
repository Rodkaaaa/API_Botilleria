from sqlalchemy.orm import Session
from app.models.botillerias_model import Botilleria

# Función para obtener todas las botillerías
def get_botillerias(db: Session):
    return db.query(Botilleria).all()

# Función para crear una botillería
def create_botilleria(db: Session, nombre: str, dueño: str, rut_empresa: str, direccion: str, horario_inicio: str, horario_termino: str):
    db_botilleria = Botilleria(
        nombre=nombre,
        dueño=dueño,
        rut_empresa=rut_empresa,
        direccion=direccion,
        horario_inicio=horario_inicio,
        horario_termino=horario_termino
    )
    db.add(db_botilleria)
    db.commit()
    db.refresh(db_botilleria)
    return db_botilleria
