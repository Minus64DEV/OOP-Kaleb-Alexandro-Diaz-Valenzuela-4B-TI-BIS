class user:
    def __init__(self, id_user, name, password):
        self.id = id_user
        self.name = name
        self._password = password
    def show_user_info(self):
        return f"User Id: {self.id} <-+-> Username: {self.name}"

    def borrow_a_book(library, book_id):
        for book in library.books:
            if (book.id == book_id):
                book.available = False
