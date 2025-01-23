class bookDef(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

class readerDef(object):
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class logbookDef(object):
    def __init__(self, id, book_id, reader_id, taken_at, returned_at):
        self.id = id
        self.book_id = book_id
        self.reader_id = reader_id
        self.taken_at = taken_at
        self.returned_at = returned_at

class answerDef(object):
    def __init__(self, book_id, name, reader_id, last_reader_full_name, in_library):
        self.book_id = book_id
        self.book_name = name
        self.last_reader_id = reader_id
        self.last_reader_full_name = last_reader_full_name
        self.in_library = in_library