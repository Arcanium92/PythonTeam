"""
Manages the full collection of books in the library and the
operations students will write tests against: adding, finding,
checking out, and returning books.
"""

from library_app.book import Book


class Catalog:
    def __init__(self):
        self._books: list[Book] = []

    @property
    def books(self) -> list[Book]:
        return list(self._books)

    def add_book(self, book: Book) -> None:
        if book is None:
            raise ValueError("book cannot be None.")
        if any(b.isbn == book.isbn for b in self._books):
            raise RuntimeError(f"A book with ISBN '{book.isbn}' already exists in the catalog.")
        self._books.append(book)

    # Build method for ISBN search
    def find_by_isbn(self, isbn: str) -> Book | None:
        return next((b for b in self._books if b.isbn == isbn), None)

    def search_by_title(self, title_query: str) -> list[Book]:
        if not title_query or not title_query.strip():
            return []
        query_lower = title_query.lower()
        return [b for b in self._books if query_lower in b.title.lower()]

    def search_by_author(self, author_query: str) -> list[Book]:
        if not author_query or not author_query.strip():
            return []
        query_lower = author_query.lower()
        return [b for b in self._books if query_lower in b.author.lower()]

    def check_out_book(self, isbn: str) -> None:
        book = self.find_by_isbn(isbn)
        if book is None:
            raise RuntimeError(f"No book found with ISBN '{isbn}'.")
        book.check_out()

    def return_book(self, isbn: str) -> None:
        book = self.find_by_isbn(isbn)
        if book is None:
            raise RuntimeError(f"No book found with ISBN '{isbn}'.")
        book.return_book()

    def total_available_copies(self) -> int:
        return sum(b.available_copies for b in self._books)
