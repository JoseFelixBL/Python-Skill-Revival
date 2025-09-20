"""
Library System

    Create classes Book, Author, and Library.
    A Book belongs to an Author (use composition).
    The Library class should manage a collection of books 
    with methods to add_book(book), remove_book(book), and 
    search_books(title="", author_name="").
"""
class Author:
    """Author class"""
    def __init__(self, author):
        self.author = author

    def get_author_info(self):
        return f"Author: {self.author}"

    def get_author(self):
        """Author name"""
        return self.author

class Book:
    """
    Book class:
        Title
        Author
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_info(self):
        """Book info"""
        book_info = [ 
            f"Title: {self.title}",
            "  " + (self.author.get_author_info())
        ]
        return "\n".join(book_info)

    def get_title(self):
        """get title"""
        return self.title

    def get_author(self):
        """Author name"""
        return self.author.get_author()

class Library:
    """
    Library class:
        List of books
    """
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        """Add a book"""
        self.collection.append(book)

    def remove_book(self, book):
        """Remove a book"""
        self.collection.remove(book) if book in self.collection else None

    def show_collection(self):
        """
        Show the list of books in library
        """
        if self.collection == []:
            return "---Colección vacía---"
        book_collection = []
        for book in self.collection:
            book_collection.append(book.get_book_info())
        return "\n".join(book_collection)

    def search_books(self, title="", author_name=""):
        """
        Search either title or author, not both (yet)
        Return the list of books
        """
        if self.collection == []:
            return "---Colección vacía---"

        book_list = []

        # for libro in self.collection:
        #     if title and libro.get_title() == title:
        #         if author_name and libro.get_author() == author_name:
        #             book_list.append(libro)
        #         else:
        #             continue
        #     if author_name and libro.get_author() == author_name:
        #         book_list.append(libro)

        for libro in self.collection:
            match (title, author_name):
                # Check how to search: title, author_name, both, none (=all books)
                case ("",""):
                    return self.collection
                case (_,""):
                    if libro.get_title() == title:
                        book_list.append(libro)
                case ("",_):
                    if libro.get_author() == author_name:
                        book_list.append(libro)
                case (_,_):
                    if libro.get_title() == title and libro.get_author() == author_name:
                        book_list.append(libro)

        return book_list


author_1 =Author("Zoé Valdés")
book_1 = Book("La nada cotidiana",  author_1)
author_2 =Author("Antonio Skármeta")
book_2 = Book("La chica del trombón",  author_2)
book_3 = Book("La boda del poeta",  author_2)

library = Library()
print(library.show_collection())

print("---")
library.remove_book(book_1)
print(library.show_collection())

print("---")
library.add_book(book_1)
print(library.show_collection())

print("---")
library.add_book(book_2)
print(library.show_collection())

print("---")
library.remove_book(book_1)
print(library.show_collection())

library.add_book(book_1)
library.add_book(book_3)

print("---")
print("==Contenido de la biblioteca:==")
print(library.show_collection())

print("---")
print(f"Buscando por título: {book_1.get_title()}")
lista = library.search_books(title=book_1.get_title())
if not lista:
    print(f"No hemos encontrado libros con título: {book_1.get_title()}")
else:
    for book in lista:
        print(book.get_book_info())

print("---")
print(f"Buscando por autor: {author_2.get_author()}")
lista = library.search_books(author_name=author_2.get_author())
if not lista:
    print(f"No hemos encontrado libros con autor: {author_2.get_author()}")
else:
    for book in lista:
        print(book.get_book_info())

print("---")
otro_autor = "Isaac Asimov"
print(f"Buscando por autor: {otro_autor}")
lista = library.search_books(author_name=otro_autor)
if not lista:
    print(f"No hemos encontrado libros con autor: {otro_autor}")
else:
    for book in lista:
        print(book.get_book_info())

print("---")
otro_titulo = "El Coronel no tiene quien le escriba"
print(f"Buscando por título: {otro_titulo}")
lista = library.search_books(title=otro_titulo)
if not lista:
    print(f"No hemos encontrado libros con título: {otro_titulo}")
else:
    for book in lista:
        print(book.get_book_info())
