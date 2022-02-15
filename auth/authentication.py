from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.hash import Hash

from db import models
from db.database import get_db
from auth import oauth2

router = APIRouter(
    tags=['authentication']
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    empleado = db.query(models.DbEmpleado).filter(models.DbEmpleado.nombre == request.username).first()
    if not empleado:
        raise HTTPException(statuscode=status.HTTP_404_NOT_FOUND, details='credenciales invalidas')
    if not Hash.verify(empleado.password, request.password):
        raise HTTPException(statuscode=status.HTTP_404_NOT_FOUND, details='password incorrecto')

    access_token =  oauth2.create_access_token(data={'sub':empleado.nombre})

    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'empleado_id': empleado.id,
        'empleado_name': empleado.nombre
    }
