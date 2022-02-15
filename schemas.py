from typing import List
from pydantic import BaseModel



class comercio(BaseModel):
    nombre: str
    email_contacto: str
    activo: bool

    class Config():
        orm_mode = True


class empleadoBase(BaseModel):
    nombre: str
    apellidos: str
    pin: str
    password: str
    activo: bool
    email: str
    comercio_id: int


# empleado inside comercioDisplay
class empleado(BaseModel):
    id: int
    nombre: str
    apellidos: str
    pin: str

    class Config():
        orm_mode = True


class empleadoDisplay(BaseModel):
    nombre: str
    apellidos: str
    pin: str
    email: str
    items: List[comercio] = []

    class Config():
        orm_mode = True


class comercioBase(BaseModel):
    nombre: str
    email_contacto: str
    activo: bool
    # creator_id: int


class comercioDisplay(BaseModel):
    nombre: str
    email_contacto: str
    activo: bool
    # empleado: empleado
    items: List[empleado] = []

    class Config():
        orm_mode = True
