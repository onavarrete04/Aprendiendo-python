from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import Table, Text

engine = create_engine("sqlite:///:memory:")

Base = declarative_base()

#Asociación de tablas
book_categories = Table("book_categories",Base.metadata,
        Column("book_id", ForeignKey("book.id"), primary_key=True),
        Column("category_id", ForeignKey("book_category.id"),primary_key=True)
)


class Author(Base):
    __tablename__= "author"
    id = Column(Integer, Sequence("author_id_seq"), primary_key="author")
    firstname = Column(String)
    lastname = Column(String)

    books=relationship('Book',  back_populates='author', cascade="all, delete, delete-orphan")
    # cascade deja no deja hijos huerfanos, es decir, si se borra al autor, se borra su libro 

    def __repr__(self) -> str:
        return "{} {}".format(self.firstname, self.lastname)

class BookCategory(Base):
    __tablename__ = "book_category"
    id = Column(Integer,Sequence("book_categoy_id_seq"),primary_key=True)
    name = Column(String)

    books = relationship("Book",
                        secondary=book_categories,
                        back_populates="categories")
    def __repr__(self):
        return "{}".format(self.name)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, Sequence("book_id_seq"), primary_key=True)
    isbn = Column(String)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))# foreing key es una llave que conecta

    author = relationship("Author", back_populates="books") 
    categories = relationship("BookCategory",secondary=book_categories,back_populates="books")

    def __repr__(self):
        return "{}".format(self.title)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

j_rowling = Author(firstname="Joanne",lastname = "Rowling")
session.add(j_rowling)
j_rowling = session.query(Author).filter_by(firstname="Joanne").one()

book =Book(
        isbn = "9789543356670",
        title = "Harry Potter y la Piedra Filosofal",
        description = "La vida de Harry Potter cambia para siempre el ...")

book.categories.append(BookCategory(name="Aventura"))
book.categories.append(BookCategory(name="Acción"))

book.author = j_rowling

print(session.query(Book).filter(Book.categories.any(name="Aventura")).all())
#
print(session.query(Book).\
        filter(Book.author==j_rowling).\
        filter(Book.categories.any(name="Aventura")).\
        all())



session.add(j_rowling)
session.commit()

"""
En este caso un libro puede tener muchas categorias y una categoria puede tener
muchos libros, por eso es una relación de muchos a muchos
"""
