from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

