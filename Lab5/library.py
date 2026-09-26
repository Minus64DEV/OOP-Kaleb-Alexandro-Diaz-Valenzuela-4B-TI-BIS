class library:
    def __init__(self):
        self.users = []
        self.books = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())