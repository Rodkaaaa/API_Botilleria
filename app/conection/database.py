from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app.conection.config import DATABASE_URL

# Obtén la URL de la base de datos desde una variable de entorno o configúralo directamente.
DATABASE_URL = DATABASE_URL

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la clase base para los modelos
Base = declarative_base()

# Función para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
