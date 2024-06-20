from fastapi import FastAPI, Depends
from Book_DB_Operations import *

app=FastAPI()



@app.post("/add_book")
async def add_new_book(b:Book):
    if Insert_Book(b):
        print("Inserted")
    return "Inserted"

@app.get("/get_books")
async def get_books():
    books = Read_Books()
    for book in books:
        print(f"ID:  {book.id} \nAuthor: {book.author} \nTitle: {book.title} \nPusblish: {book.published_year}")
    return books


@app.get("/get_book/{book_id}")
async def get_book(book_id:int):      
    book = Search_Book(book_id)
    if book:
        return book   
    else:
        return "Not Found!"
            

@app.put("/Edit_book/{book_id}")
async def edit_book(b:Book):
    if Update_book(b):
        return "Updated!"
    else:
        return "Can't Update"


@app.delete("/delete_book/{book_id}")
async def Delete_book(book_id:int):
    if delete_book(book_id):
        print("Deleted!")
        return "Deleted!"
    else:
        print("Can't Delete the book") 
    return "can't delete!"