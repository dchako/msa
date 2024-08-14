from sqlalchemy.orm import Session
from . import models, schemas

def create_calculo_escanos(db: Session, calculo: schemas.CalculoEscanosCreate):
    db_calculo = models.CalculoEscanos(
        escaños=calculo.escaños,
        votos=str(calculo.votos),
        resultado=str(calcular_dhondt(calculo.votos, calculo.escaños))
    )
    db.add(db_calculo)
    db.commit()
    db.refresh(db_calculo)
    return db_calculo

def get_calculos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CalculoEscanos).offset(skip).limit(limit).all()

def calcular_dhondt(votos: Dict[str, int], escaños: int) -> Dict[str, int]:
    escaños_asignados = {lista: 0 for lista in votos.keys()}
    votos_restantes = [(lista, votos[lista]) for lista in votos.keys()]

    for _ in range(escaños):
        lista_ganadora, max_votos = max(votos_restantes, key=lambda x: x[1])
        escaños_asignados[lista_ganadora] += 1

        for i, (lista, votos_lista) in enumerate(votos_restantes):
            if lista == lista_ganadora:
                votos_restantes[i] = (lista, votos_lista / (escaños_asignados[lista] + 1))
                break

    return escaños_asignados
