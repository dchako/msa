from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/calcular", response_model=schemas.CalculoEscanos)
def calcular_escaños(calculo: schemas.CalculoEscanosCreate, db: Session = Depends(database.get_db)):
    return crud.create_calculo_escanos(db=db, calculo=calculo)

@router.get("/historial", response_model=List[schemas.CalculoEscanos])
def leer_historial(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_calculos(db=db, skip=skip, limit=limit)

@router.get("/calculo/{calculo_id}", response_model=schemas.CalculoEscanosDetalle)
def leer_calculo(calculo_id: int, db: Session = Depends(database.get_db)):
    calculo = db.query(models.CalculoEscanos).filter(models.CalculoEscanos.id == calculo_id).first()
    if not calculo:
        raise HTTPException(status_code=404, detail="Cálculo no encontrado")
    
    calculo.votos = eval(calculo.votos)
    calculo.resultado = eval(calculo.resultado)
    
    return calculo
