from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session

Base = declarative_base()

class Author(Base):

    __tablename__ = "author"
    id = Column(Integer,Sequence("author_id_seq"),primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return "{} {}".format(self.firstname,self.lastname)

engine = create_engine("sqlite:///:memory:")

Base.metadata.create_all(engine) # se esta en la condición de comunicarse con la base de datos
# la comunicación se hace a travez de una sesión

Session = sessionmaker(bind=engine) # sirve para crear varias sesiones, la conexión estara hasta que se
# haga un commit o se cierre la sessión
session = Session()

author = Author(firstname="Joanne", lastname = "Rowling")

session.add(author)

our_author = session.query(Author).filter_by(firstname="Joanne").first()
print(author is our_author)

session.add_all([
Author(firstname='John Ronald Reuel', lastname='Tolkien'),
Author(firstname='Jose', lastname='Hernandez')
]) #-> manda para guardar

# session.new -> muestra los autores que estan por guardar y que estan todavia en la sesion
# session.dirty -> objetos modificados MOOODIFICADOS en la sesion y todavia no guardadso en la base de datos
#session.commit() -> se envia todos los cambios a la base de datos y se devuelve la conexion al pull de conexiones
#author.id -> muestra si tiene id, cuando esta en la sesión no tiene id, pero cuando esta en la base de datos si tiene
#  todos los identificadores de la base de datos estan en la instancia
# session.rollback() -> reviertes cambios que estan en la sesion