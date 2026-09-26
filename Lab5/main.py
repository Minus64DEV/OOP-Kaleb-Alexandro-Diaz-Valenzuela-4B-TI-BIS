import books as b, library as l, users as u

mainlib = l.library()

book1 = b.book("001", "OOP Fundamentals", "John L", "BBC")
book2 = b.book("002", "Python for dummies", "Stef Maruch", "For Dummies")

user1 = u.user("001", "Kaleb Díaz", "1234")

mainlib.add_book(book1)
mainlib.add_book(book2)
mainlib.add_user(user1)

mainlib.show_books()
mainlib.show_users()

#Requirementes
#1.- The system must allow register books.
#2.- The system must allow register users.
#3.- The system must allow a book to be borrow by an user.
#4.- A book that has already been borrowed canot be borrowed again
#5.- The sistem must allow a book to be returned