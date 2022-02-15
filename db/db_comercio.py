from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import comercioBase
from db.models import DbComercio


def create_comercio(db: Session, request: comercioBase):
    new_comercio = DbComercio(
        nombre=request.nombre,
        email_contacto=request.email_contacto,
        activo=request.activo,
    )
    db.add(new_comercio)
    db.commit()
    db.refresh(new_comercio)
    return new_comercio

def get_all_comercios(db: Session):
    comercio = db.query(DbComercio).all()
    return comercio

def get_comercio(db: Session, id: int):
    comercio = db.query(DbComercio).filter(DbComercio.id == id).first()
    # Exceptions
    return comercio
