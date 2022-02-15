from fastapi import FastAPI

from auth import authentication
from router import empleado, comercio
from db import models
from db.database import engine

app = FastAPI()
app.include_router(authentication.router)
app.include_router(empleado.router)
app.include_router(comercio.router)


models.Base.metadata.create_all(engine)

