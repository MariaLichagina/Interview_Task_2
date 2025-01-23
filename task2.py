
from fastapi import FastAPI, HTTPException, Response
import sqlite3
import db
import json
from model import answerDef


db.init()

app = FastAPI()

@app.get("/library/book/{book_id}/status")
def getLogbook(book_id: int):
    logbook = db.getLogbookByBookId(book_id)
    if logbook == None:
        raise HTTPException(status_code=404, detail="logbook not found")
    book = db.getBookById(book_id)
    reader = db.getReaderById(logbook.reader_id)

    answer = answerDef(logbook.book_id, book.name, logbook.reader_id, reader.first_name + ' ' + reader.last_name, logbook.returned_at)
    print(answer.last_reader_full_name)
    json_answer = json.dumps(answer.__dict__, ensure_ascii=False, indent=4)

    return Response(json_answer, media_type="application/json")

 