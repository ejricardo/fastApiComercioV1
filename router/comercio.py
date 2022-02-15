from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import db_comercio
from db.database import get_db
from schemas import comercioBase, comercioDisplay, empleadoBase
from auth.oauth2 import oauth2_scheme, get_current_empleado

router = APIRouter(
    prefix='/comercio',
    tags=['comercio']
)

# create comercio
@router.post('/', response_model=comercioDisplay)
def create_comercio(request: comercioBase, db: Session = Depends(get_db)):
    return db_comercio.create_comercio(db, request)


# Read all comercio
@router.get('/', response_model=List[comercioDisplay])
def get_all_comercios(db: Session = Depends(get_db)):
    return db_comercio.get_all_comercios(db)

# get specific comercio
@router.post('/{id}')#, response_model=comercioDisplay)
def get_comercio(id:int, db: Session = Depends(get_db),  current_empleado: empleadoBase = Depends(oauth2_scheme)): # Depends(get_current_empleado)):
    return {
        'data': db_comercio.get_comercio(db, id),
        'current_empleado': current_empleado
    }




