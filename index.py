class LibraryBook:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

    def display_info(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)


book1 = LibraryBook("Python Programming", "John Smith", 101)
book2 = LibraryBook("Data Science with Python", "Jane Doe", 102)
book3 = LibraryBook("Machine Learning Basics", "Alice Johnson", 103)

book1.display_info()
book2.display_info()
book3.display_info()