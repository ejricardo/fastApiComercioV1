from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from db.hash import Hash
from schemas import empleadoBase
from db.models import DbEmpleado


def create_empleado(db: Session, request: empleadoBase):
    new_empleado = DbEmpleado(
        nombre=request.nombre,
        apellidos=request.apellidos,
        pin=request.pin,
        email=request.email,
        password=Hash.bcrypt(request.password),
        comercio_id=request.comercio_id
    )
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado


def get_all_empleados(db: Session):
    return db.query(DbEmpleado).all()


def get_empleado(db: Session, id: int):
    return db.query(DbEmpleado).filter(DbEmpleado.id == id).first()


def get_empleado_by_nombre(db: Session, nombre: str):
    empleado = db.query(DbEmpleado).filter(DbEmpleado.id == id).first()
    if not empleado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'empleado con nombre {nombre} no encontrado'
                            )
    return empleado


def update_empleado(db: Session, id: int, request: DbEmpleado):
    empleado = db.query(DbEmpleado).filter(DbEmpleado.id == id)
    empleado.update({
        DbEmpleado.nombre: request.nombre,
        DbEmpleado.apellidos: request.apellidos,
        DbEmpleado.pin: request.pin,
        DbEmpleado.email: request.email,
        DbEmpleado.password: Hash.bcrypt(request.password),
        DbEmpleado.activo: request.activo
    })
    db.commit()
    return 'ok'


def delete_empleado(db: Session, id: int):
    empleado = db.query(DbEmpleado).filter(DbEmpleado.id == id).first()
    db.delete(empleado)
    db.commit()
    return 'ok'
