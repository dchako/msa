from fastapi import FastAPI
from .database import engine
from . import models
from .routers import escaños

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(escaños.router)
