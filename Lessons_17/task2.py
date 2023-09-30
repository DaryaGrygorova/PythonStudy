"""Task 2 - Library

Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book
class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
"""


class Library:
    """Create library object with methods: new_book, group_by_author, group_by_year"""

    def __init__(self):
        self.library = {}

    def __repr__(self):
        return f"{self.library}"

    def __str__(self):
        return f"My lib: {self.library}"

    def new_book(self, name, year, author):
        """Returns an instance of Book class
        and adds the book to the books list for the current library"""
        if name in self.library:
            print(f'Book with name "{name}" is already in the library\n')
            return None
        new_book = Book(author, name, year)
        self.library[name] = new_book
        if name not in author.books:
            author.books.append(name)
        return new_book

    def group_by_author(self, author):
        """Returns a list of all books grouped by the specified author"""
        return [
            book_name
            for book_name, info in self.library.items()
            if info.author == author
        ]

    def group_by_year(self, year):
        """Returns a list of all the books grouped by the specified year"""
        return [info for _, info in self.library.items() if info.year == year]


class Book:
    """Create book object"""

    def __init__(self, author, name, year):
        self.author = author
        self.name = name
        self.year = year

    def __repr__(self):
        return f"'{self.author}', {self.year}"

    def __str__(self):
        return f'Book "{self.name}", written by {self.author} in {self.year} year'


class Author:
    """Create author object"""

    def __init__(self, name, birthday, books, country):
        self.name = name
        self.birthday = birthday
        self.books = books or []
        self.country = country

    def __repr__(self):
        return (
            f"'name': {self.name}, 'birthday': {self.birthday}, "
            f"'books': {self.books},'country': {self.country}"
        )

    def __str__(self):
        return f"{self.name}"


author_1 = Author(
    "David Alan Nicholls",
    "11.30.1966",
    ["One day", "Us"],
    "Great Britain",
)
author_2 = Author(
    "Colleen McCullough",
    "06.01.1937",
    ["The Ladies of Missalonghi", "The Prodigal Son"],
    "Australia",
)
author_3 = Author("Margaret Mitchell", "11.08.1900", ["Gone with the Wind"], "USA")

my_lib = Library()
my_lib.new_book("One day", 2019, author_1)
my_lib.new_book("One day", 2019, author_1)
my_lib.new_book("Sweet Sorrow", 2019, author_1)
my_lib.new_book("Us", 2014, author_1)
my_lib.new_book("The Thorn Bird", 1977, author_2)
my_lib.new_book("Gone with the Wind", 1936, author_3)

print("Books in my library:", my_lib, sep="\n")

print(f"\nBooks written by {author_1}:")
print("In lib:", my_lib.group_by_author(author_1))
print("In author object: ", author_1.books)

print(f"\nBooks written by {author_2}:")
print("In lib:", my_lib.group_by_author(author_2))
print("In author object: ", author_2.books)

print("\nBooks published in 1977:", my_lib.group_by_year(1977))
print("\nBooks published in 2019:", my_lib.group_by_year(2019))
