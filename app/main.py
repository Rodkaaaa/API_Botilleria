from fastapi import FastAPI
from app.routers import botillerias , usuarios, productos
from app.conection.database import engine
from app.models import botillerias_model, usuarios_model, productos_model


botillerias_model.Base.metadata.create_all(bind=engine)
productos_model.Base.metadata.create_all(bind=engine)
usuarios_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(botillerias.router)
app.include_router(usuarios.router)
app.include_router(productos.router)
