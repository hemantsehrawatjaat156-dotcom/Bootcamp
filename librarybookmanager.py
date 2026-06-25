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