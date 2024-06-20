from Model import *
from pydantic import BaseModel, constr
from sqlalchemy.exc import SQLAlchemyError


class Book(BaseModel):
   id:int
   title: str
   author:str
   published_year: str
   class Config:
      orm_mode = True # Note: the use of orm_mode=True in the config class indicating that it is mapped with the ORM class of SQLAlchemy.

# insert 
def Insert_Book(book:Book):
    New_Book = Books(title = book.title , author = book.author , published_year = book.published_year)
    flag : bool
    try:
        session = Session()
        session.add(New_Book)
        session.commit()
        session.refresh(New_Book)
        session.close()
        flag = True
    except SQLAlchemyError as e:
         print(f"Can't  Insert User for this error: {e}")
         flag = False 
    return flag

# Read 

def Read_Books():
        try:
                session = Session()
                books = session.query(Books).all()
                session.close()
                print("Readed!")               
        except SQLAlchemyError as e:
                print(f"Can't  Insert User for this error: {e}")
        return books



# Search
def Search_Book(id:int):
        flag : bool 
        try:
                session = Session()
                book = session.query(Books).filter(Books.id == id).first()
                session.close()
                if book:
                        print("Found!")
                        flag = True
                else:
                        print("Not Found!")
                        flag = False 
        except SQLAlchemyError as e:
                print(f"Can't  Insert User for this error: {e}")
                flag = False 
                return flag
        return book

# Update 
def Update_book(b: Book):
        flag : bool
        try:
                session = Session()
                book = session.query(Books).filter(Books.id == b.id).first()
                if book:
                        book.title = b.title
                        book.author = b.author
                        book.published_year = b.published_year
                        session.commit()  
                        session.close()        
                        print("Updated")
                        flag = True
                else:
                        print(" this book not found!")
                        flag = False
        except SQLAlchemyError as e:
                print(f"Can't update book for this error: {e}")
                flag = False 
        return flag

# Delete
def delete_book(id:int):
        flag : bool
        try:
                session = Session()
                book = session.query(Books).filter(Books.id == id).first()
                if book:
                        session.delete(book)
                        session.commit()
                        session.close()
                        print("Deletedfff!")
                        flag = True
                else:
                        print("Book Not Found!")        
                        flag = False      
        except SQLAlchemyError as e:
                print(f"Can't update book for this error: {e}")
                flag = False 
        return flag              