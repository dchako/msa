from pydantic import BaseModel
from typing import List, Dict

class CalculoEscanosBase(BaseModel):
    escaños: int
    votos: Dict[str, int]

class CalculoEscanosCreate(CalculoEscanosBase):
    pass

class CalculoEscanos(CalculoEscanosBase):
    id: int
    resultado: Dict[str, int]

    class Config:
        orm_mode = True

class CalculoEscanosDetalle(BaseModel):
    id: int
    escaños: int
    votos: Dict[str, int]
    resultado: Dict[str, int]

    class Config:
        orm_mode = True
