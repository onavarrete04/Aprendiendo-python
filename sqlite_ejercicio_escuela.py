# encoding uft-8


# Se importan las librerias

from datetime import datetime
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import Table, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime



engine = create_engine("sqlite:///:memory:")

Base = declarative_base()

# Relación Muchos a Muchos 

# Horario <-> Cursos 
association_tabla_horario_curso = Table('association_tabla_horario_Curso ', Base.metadata,
 Column('horario_id', Integer, ForeignKey('horario.id_horario'),primary_key=True),
 Column('curso_id', Integer, ForeignKey('curso.id_curso'),primary_key=True)
)

# Relacion uno a uno


# Alumno <-> Curso



class Horario(Base):
    __tablename__ = "horario"
    id_horario = Column(Integer, Sequence("id_horario"), primary_key=True)
    nombre_dia = Column(String)
    fecha_inicio = Column(String)
    fecha_final = Column(String)

    # Muchos a muchos
    asociacion_c = relationship("Curso", secondary=association_tabla_horario_curso,
                                            back_populates="asociacion_h")
    # cascade="all, delete, delete-orphan" no esta soportado en relaciones de muchos a muchos

    # Uno a uno
    asociacion_ph = relationship("Profesor", back_populates="asociacion_hp", uselist=False)

    def __repr__(self):
        return "{} {} {}".format(self.nombre_dia, self.fecha_final, self.fecha_final)


class Curso(Base):
    __tablename__ = "curso"
    id_curso = Column(Integer, Sequence("id_curso"), primary_key=True)
    nombre_curso = Column(String)

    asociacion_h = relationship('Horario', back_populates='asociacion_c', secondary=association_tabla_horario_curso)
    asociacion_al = relationship("Alumno", back_populates="asociacion_ca", uselist=False)
    # Las relaciones de uno a uno se utiliza uselist False
    
    asociacion_p = relationship("Profesor",back_populates="asociacion_cp")

    def __repr__(self):
        return "{}".format(self.nombre_curso)
class Alumno(Base):
    __tablename__ = "alumno"
    id_alumno = Column(Integer, Sequence("id_alumno"), primary_key=True)
    nombre_alumno = Column(String)
    documento_alumno = Column(String)
    FK_id_curso = Column(Integer,ForeignKey("curso.id_curso"))

    asociacion_ca = relationship('Curso', back_populates='asociacion_al')

    def __repr__(self):
        return "{}".format(self.nombre_alumno)

class Profesor(Base):
    __tablename__ = "profesor"
    id_profesor= Column(Integer, Sequence("id_profesor"), primary_key=True)
    nombre_profesor = Column(String)
    documento_profesor = Column(String)
    FK_id_curso = Column(Integer,ForeignKey("curso.id_curso"))
    FK_id_horario= Column(Integer,ForeignKey("horario.id_horario"))
    
    asociacion_cp = relationship('Curso', back_populates='asociacion_p')
    asociacion_hp = relationship('Horario', back_populates='asociacion_ph')

    def __repr__(self):
        return "{}".format(self.nombre_profesor)

# CORRER PROGRAMA

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

horarios = Horario(nombre_dia = "Lunes", fecha_inicio = "06/01/2022 08:00",
                     fecha_final="06/01/2022 08:00")
cursos = Curso(nombre_curso = "Algoritmos introducción a la programación")

profesores = Profesor(nombre_profesor = "Fernando Hernandez",
                    documento_profesor= "987654321")

session.add(horarios)
session.add(cursos)

session.add(profesores)

horarios = Horario(nombre_dia = "Jueves", fecha_inicio = "13/01/2022 13:00",
                     fecha_final="13/01/2022 16:00")
cursos = Curso(nombre_curso = "SQLserver")
alumnos = Alumno(nombre_alumno = "Angela Oscarina", documento_alumno ="3456123")
profesores = Profesor(nombre_profesor = "Ruth Serina",
                    documento_profesor= "42216868")
session.add(horarios)
session.add(cursos)
session.add(alumnos)
session.add(profesores)

cursos.asociacion_al =  Alumno(nombre_alumno = "Camila Andrea Gonzales",
                         documento_alumno ="123456")

session.add(cursos)

cursos.asociacion_al =  Alumno(nombre_alumno = "Oscar Barreto",
                         documento_alumno ="1209876")

session.add(cursos)
session.commit()

print("Consulta 1: Alumnos que pertenecen a un curso")



for alumn, course in session.query(Alumno,Curso).filter(Alumno.id_alumno).all():
    print(alumn)
            
"""for i in session.query(Alumno,Curso).all():
    print(i)"""

"""print(session.query(Horario).join(Curso).\
            filter(Curso.id_curso==1).\
            all())"""


print("-------")
print(session.query(Horario).all())
print(session.query(Curso).all())
print(session.query(Alumno).all())
print(session.query(Profesor).all())
          



"""
Relaciones de las bases de datos

1) De muchos a muchos Cursos y Horario
2) De uno a uno Alumno y Curso
3) De uno a uno Horario a Profesor
3) De uno a muchos Curso y Profesor

"""