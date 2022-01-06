from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session

engine = create_engine("sqlite:///:memory:")

Base = declarative_base()

class Author(Base):
    __tablename__= "author"
    id = Column(Integer, Sequence("author_id_seq"), primary_key="author")
    firstname = Column(String)
    lastname = Column(String)

    books=relationship('Book',  back_populates='author') 

    def __repr__(self) -> str:
        return "{} {}".format(self.firstname, self.lastname)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, Sequence("book_id_seq"), primary_key=True)
    isbn = Column(String)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))# foreing key es una llave que conecta

    author = relationship("Author", back_populates="books") #  se variable en el que se hace la relación con Author y books
    # en relationship no se soporto order_by="Books.id", da error por elemento inesperado

    def __repr__(self):
        return "{}".format(self.title)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

j_rowling = Author(firstname="Joanne",lastname = "Rowling")
print(j_rowling.books)

j_rowling.books = [Book(
        isbn = "9789543356670",
        title = "Harry Potter y la Piedra Filosofal",
        description = "La vida de Harry Potter cambia para siempre el ..."),
        Book(
        isbn = "9345527097214",
        title = "Harry Potter y la Cámara Secreta",
        description = "Tras derrotar una vez más a lord Voldermort ..."

)]

print(j_rowling.books[1])
print(j_rowling.books[1].title)

session.add(j_rowling)
session.commit()

j_rowling = session.query(Author).filter_by(firstname="Joanne").one()
print(j_rowling.books)