class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Kitob nomi: {self.title}, Muallif: {self.author}, Narxi: {self.price} so'm")

class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} {self.name} do'koniga qo'shildi.")

    def display_books(self):
        print(f"{self.name} do'konida mavjud kitoblar:")
        for book in self.books:
            book.display_info()

# Test qismi
book1 = Book("Sherlock Holmes", "Arthur Conan Doyle", 30000)
book2 = Book("War and Peace", "Leo Tolstoy", 25000)

bookstore = Bookstore("Kitob Olami")
bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.display_books()

if __name__ == '__main__':
    pass