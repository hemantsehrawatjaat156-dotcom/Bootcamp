class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.__copies = copies

    def isbn(self):
        return self.__isbn

    def available(self):
        return self.__copies

    def checkout(self, n):
        if n > self.__copies:
            raise ValueError("Not enough copies")
        self.__copies -= n
        print("Checked out:", n)

    def return_book(self, n):
        self.__copies += n
        print("Returned:", n)

b = Book("123", "Python", "XYZ", 5)
b.checkout(2)
b.return_book(1)
print(b.available())