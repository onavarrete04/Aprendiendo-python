from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists

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

session.add(j_rowling)
session.commit()

# Consultas - query
print("Consulta 1:")
for an_author, a_book in session.query(Author,Book).\
                filter(Author.id==Book.author_id).\
                filter(Book.isbn=="9789543356670").all():
            print(an_author)
            print(a_book)
print("Consulta 2:")
print(session.query(Author).join(Book).\
            filter(Book.isbn=="9789543356670").\
            all())
print("Consulta 3:")
print(session.query(Author).join(Book, Author.id == Book.author_id).all()) # condición explicita
print("Consulta 4:")
print(session.query(Author).join(Author.books).all())
print("Consulta 5:")
print(session.query(Author).join(Author.books).all())
print("Consulta 6:")
print(session.query(Author).join("books").all()) # usando un string
print("Consulta 7:")
stmt = exists().where(Book.author_id==Author.id)
for name, in session.query(Author.firstname).filter(stmt):
    print(name)
print("Consulta 8:")
for name, in session.query(Author.firstname).filter(Author.books.any()): # usando any
    print(name)
print("Consulta 9:")
for name, in session.query(Author.firstname).\
            filter(Author.books.any(Author.lastname.like("%Row%"))):
    print(name)
print("Consulta 10:")
print(session.query(Book).filter(~Book.author.has(Author.firstname=="Joanne")).all())
print("----")
print(session.query(Author.firstname,Author.lastname).count())
for autor in session.query(Author.firstname,Author.lastname):
    print(autor)
