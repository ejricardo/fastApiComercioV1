from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column


class DbEmpleado(Base):
    __tablename__ = 'empleado'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellidos = Column(String)
    pin = Column(String)
    email = Column(String)
    password = Column(String)
    activo = Column(Boolean, default=True)
    comercio_id = Column(Integer, ForeignKey('comercio.id'))
    comercio = relationship('DbComercio', back_populates='items')


class DbComercio(Base):
    __tablename__ = 'comercio'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email_contacto = Column(String)
    activo = Column(Boolean, default=True)
    items=relationship('DbEmpleado', back_populates='comercio')
