from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = int(year)
        self.isbn = isbn

    def __repr__(self) -> str:
        return (
            f"Book(title='{self.title}', "
            f"author='{self.author}', "
            f"year={self.year}, "
            f"isbn='{self.isbn}')"
        )


class LibraryCatalog:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book

    def remove_book(self, isbn: str):
        self.books.pop(isbn, None)

    def find_by_title(self, keyword: str) -> List[Book]:
        keyword = keyword.lower()

        return [
            book
            for book in self.books.values()
            if keyword in book.title.lower()
        ]

    def find_by_author(self, author_name: str) -> List[Book]:
        author_name = author_name.lower()

        return [
            book
            for book in self.books.values()
            if book.author.lower() == author_name
        ]

    def list_all(self) -> List[Book]:
        return sorted(
            self.books.values(),
            key=lambda book: book.title.lower()
        )


if __name__ == "__main__":
    catalog = LibraryCatalog()

    # Adding five diverse books
    catalog.add_book(
        Book(
            "Python Crash Course",
            "Eric Matthes",
            2019,
            "9781593279288"
        )
    )

    catalog.add_book(
        Book(
            "Clean Code",
            "Robert C. Martin",
            2008,
            "9780132350884"
        )
    )

    catalog.add_book(
        Book(
            "The Alchemist",
            "Paulo Coelho",
            1988,
            "9780061122415"
        )
    )

    catalog.add_book(
        Book(
            "Atomic Habits",
            "James Clear",
            2018,
            "9780735211292"
        )
    )

    catalog.add_book(
        Book(
            "The Pragmatic Programmer",
            "Andrew Hunt",
            1999,
            "9780135957059"
        )
    )

    # Search by title
    print("=== Search by Title ===")
    title_results = catalog.find_by_title("python")

    for book in title_results:
        print(book)

    # Search by author
    print("\n=== Search by Author ===")
    author_results = catalog.find_by_author("James Clear")

    for book in author_results:
        print(book)

    # Full sorted list
    print("\n=== All Books Sorted by Title ===")

    for book in catalog.list_all():
        print(book)