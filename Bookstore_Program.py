#T39 - Bookstore Program

import sqlite3
db = sqlite3.connect('T39\\bookstore')
cursor = db.cursor() 

#========create the database structure==========
cursor = db.cursor() 
cursor.execute('''
CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, quantity INTEGER)
''')
db.commit()

#======populate database with given entries======
booklist = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),(3002, 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40),(3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),(3004, 'The Lord of the Rings', 'J.R.R. Tolkein', 37),(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]
cursor.executemany(''' INSERT OR REPLACE INTO bookstore(id, Title, Author, quantity) VALUES(?,?,?,?)''',
booklist)
db.commit()

#=====defining empty variables======
title_change = 'nil'
author_change = 'nil'
title_change = 0
yep=['y','Y']

#======defining functions===========
#enter a new book function 
def book_enter():
    new_id = int(input('Enter the new id number: '))
    new_Title = input('Enter the title of the book: ').capitalize()
    new_Author = input('Enter the name of the author: ').capitalize()
    new_quantity = int(input('Enter the number of books: '))

    cursor.execute(''' INSERT INTO bookstore VALUES(?, ?, ?, ?)''', (new_id, new_Title, new_Author, new_quantity))
    db.commit()

#update existing book function
def book_update():
    update_id = int(input('Enter the id number of the book you wish to update: '))
    #data validation
    #print book information
    cursor.execute('''SELECT Title, Author, quantity FROM bookstore WHERE id=?''', (update_id,))
    book = cursor.fetchone()
    print(book)
    #type in new information fields
    confirm = str(input('Type Y if this is the book you wish to update: '))
    if confirm in yep:
        title_change = input('Enter the updated title: ')
        author_change = input('Enter the updated author: ')
        quantity_change = int(input('Enter the updated quantity: '))
        change = [title_change, author_change, quantity_change, update_id]
        #update record
        cursor.execute('''UPDATE bookstore SET id =?,Title =?,Author =?,quantity =? 
        WHERE id =?''',(update_id, title_change, author_change, quantity_change, update_id))
        db.commit()
    else:
        exit()
        
#delete an existing book function
def book_delete():
    id = int(input('Enter the id number of the book you wish to update: '))
    cursor.execute('''SELECT Title, Author, quantity FROM bookstore WHERE id=?''', (id,))
    book = cursor.fetchone()
    print(book)
    confirm = str(input('Type Y if this is the book you wish to update: '))
    if confirm in yep:
        cursor.execute('''DELETE FROM bookstore WHERE id=?''', (id,))
        print('Record Deleted')
    else:
        exit()

#Search for a book function
def list_books():
    # Display data 
        print("STUDENT Table: ")
        data=cursor.execute('''SELECT * FROM bookstore''')
        for row in data:
            print(row)

#menu exit function
def menu_Exit():
    db.close()
    exit()

#book_id = int(input('enter book id: '))
#cursor.execute('''SELECT Title, Author, quantity FROM bookstore WHERE id=?''', (book_id,))
#student = cursor.fetchone()
#print(student)

while True:

    menu = input('''Select one of the following Options below:
    e  - enter a new book
    u  - update existing record
    d  - delete an existing record
    l  - list books
    x  - exit
    : ''').lower()

    if menu == 'e':
        book_enter()
    elif menu == 'u':
        book_update()
    elif menu == 'd':
        book_delete()       
    elif menu == 'l':
        list_books()
    elif menu == 'x':
        db.close()
        exit()
