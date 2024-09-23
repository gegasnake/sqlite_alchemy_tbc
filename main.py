from sqlalchemy import create_engine, Table, Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from faker import Faker
import random

# The difference between the previous exercise's and this solution is that this is more class based and depends on
# the class methods sqlAlchemy provides for us. we created the columns with the help of Column like we will do in django
# in the future with the help of the fields.

fake = Faker()
Base = declarative_base()
engine = create_engine('sqlite:///books_authors.db')
Session = sessionmaker(bind=engine)
session = Session()

# Association table for the many-to-many relationship between authors and books
author_book_association = Table(
    'author_book', Base.metadata,
    Column('author_id', Integer, ForeignKey('author.id')),
    Column('book_id', Integer, ForeignKey('book.id'))
)


# Author model
class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    birth_place = Column(String)

    books = relationship('Book', secondary=author_book_association, back_populates='authors')


# Book model
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    pages = Column(Integer)
    publish_date = Column(Date)

    # creating a relationship with author
    authors = relationship('Author', secondary=author_book_association, back_populates='books')


# Create the tables in the database
Base.metadata.create_all(engine)


def generate_random_authors(n):
    """Function to generate random authors and save to the database."""
    for _ in range(n):
        author = Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birth_date=fake.date_of_birth(minimum_age=20, maximum_age=80),
            birth_place=fake.city()
        )
        session.add(author)
    session.commit()


def generate_random_books(n):
    """Function to generate random books and assign random authors."""
    authors = session.query(Author).all()

    for _ in range(n):
        book = Book(
            title=fake.sentence(nb_words=3),
            category=random.choice(['Fiction', 'Science', 'Technology', 'History', 'Fantasy']),
            pages=random.randint(100, 1000),
            publish_date=fake.date_between(start_date='-50y', end_date='today')
        )
        book.authors = random.sample(authors, random.randint(1, 3))
        session.add(book)
    session.commit()


# Generate random authors and books
generate_random_authors(500)
generate_random_books(1000)

# Query for the book with the most pages
max_pages_book = session.query(Book).order_by(Book.pages.desc()).first()
print("Book with most pages:", max_pages_book.title, max_pages_book.pages)

# Query for the average number of book pages
avg_pages = session.query(func.avg(Book.pages)).scalar()
print("Average number of pages in books:", avg_pages)

# Query for the youngest author
youngest_author = session.query(Author).order_by(Author.birth_date.desc()).first()
print("Youngest author:", youngest_author.first_name, youngest_author.last_name, youngest_author.birth_date)

# Query for authors without books
authors_without_books = session.query(Author).filter(~Author.books.any()).all()
print("Authors without books:", [(author.first_name, author.last_name) for author in authors_without_books])

# Query for top 5 authors who have written more than 3 books
authors_with_more_than_3_books = session.query(Author).join(Author.books).group_by(Author.id).having(
    func.count(Book.id) > 3).limit(5).all()
print("Authors with more than 3 books:",
      [(author.first_name, author.last_name) for author in authors_with_more_than_3_books])

# Close the session
session.close()
