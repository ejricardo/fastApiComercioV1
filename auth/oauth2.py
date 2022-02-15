from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from db import db_empleado
from db.database import get_db
from fastapi import HTTPException, status

# run -> openssl rand -hex 32

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '77407c7339a6c00544e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_empleado(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        # header={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        nombre: str = payload.get('sub')
        if nombre is None:
            raise credentials_exceptions
    except JWTError:
        raise credentials_exceptions

    empleado = db_empleado.get_empleado_by_nombre(db, nombre)

    if empleado is None:
        raise credentials_exceptions

    return empleado

