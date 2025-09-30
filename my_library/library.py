class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        self.books.append((title, author))
        return f"{title},from {author} added to {self.name} library"

    def remove_book(self, title, author):
        if (title, author) in self.books:
            self.books.remove((title, author))
            return f"{title},from {author} removed from {self.name} library"
        else:
            return "Book not found"
        
    def search_book(self, title, author):            
        if (title, author) in self.books:
            return f"{title},from {author} is available in {self.name} library"
        else:
            return "Book not found"
        
    def show_books(self):
        if not self.books:
            print( "No book in the library")
        for i, (title, author) in enumerate(self.books, start = 1):
            print (f"{i}. '{title}' by {author} \n")