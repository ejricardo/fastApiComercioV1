from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import db_empleado
from db.database import get_db
from schemas import empleadoBase, empleadoDisplay

router = APIRouter(
    prefix='/empleado',
    tags=['empleado']
)


# Create empleado
@router.post('/', response_model=empleadoDisplay)
def create_empleado(request: empleadoBase, db: Session = Depends(get_db)):
    return db_empleado.create_empleado(db, request)


# Read all empleado
@router.get('/', response_model=List[empleadoDisplay])
def get_all_empleados(db: Session = Depends(get_db)):
    return db_empleado.get_all_empleados(db)


# Read empleado
@router.get('/{id}', response_model=empleadoDisplay)
def get_empleado(id: int, db: Session = Depends(get_db)):
    return db_empleado.get_empleado(db, id)

# Update empleado
@router.post('/{id}/update')
def update_empleado(id: int, request:  empleadoBase, db: Session = Depends(get_db)):
    return db_empleado.update_empleado(db, id, request)

# Delete empleado

@router.post('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_empleado.delete_empleado(db, id)
