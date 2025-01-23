import sqlite3
from model import bookDef, readerDef, logbookDef


conn = sqlite3.connect('example.db', check_same_thread=False)

def init():
    cursor = conn.cursor()

 
    cursor.execute('''
    DROP TABLE IF EXISTS books
    ''')

    cursor.execute('''
    DROP TABLE IF EXISTS readers
    ''')   

    cursor.execute('''
    DROP TABLE IF EXISTS logbook
    ''')         


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS readers (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL       
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logbook (
        id INTEGER PRIMARY KEY,
        reader_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        taken_at DATE NOT NULL,
        returned_at DATE
    )
    ''')

    cursor.execute('INSERT INTO books (id, name) VALUES (?, ?)', (1, 'Страна багровых туч'))
    cursor.execute('INSERT INTO readers (id, first_name, last_name) VALUES (?, ?, ?)', (1, 'Алексей', 'Иванов'))
    cursor.execute('INSERT INTO logbook (reader_id, book_id, taken_at, returned_at) VALUES (?, ?, ?, ?)', (1, 1, '2025-01-09', None))
    conn.commit()

def getLogbookByBookId(bookId):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logbook where book_id = ? order by taken_at desc limit 1', (bookId, ))
    result = cursor.fetchone()
    if result == None:
        return None
    return logbookDef(*result)

def getBookById(id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books where id = ?', (id, ))
    result = cursor.fetchone()
    if result == None:
        return None
    return bookDef(*result)

def getReaderById(id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM readers where id = ?', (id, ))
    result = cursor.fetchone()
    if result == None:
        return None
    return readerDef(*result)