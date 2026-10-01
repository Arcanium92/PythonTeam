"""
Console app entry point demonstrating the library checkout system.
Run with: python main.py
"""

from library_app.book import Book
from library_app.catalog import Catalog


def main():
    catalog = Catalog()

    catalog.add_book(Book("The Pragmatic Programmer", "David Thomas", "9780135957059", 3))
    catalog.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884", 2))
    catalog.add_book(Book("The DevOps Handbook", "Gene Kim", "9781942788003", 1))

    print("=== Library Catalog ===")
    for book in catalog.books:
        print(f"{book.title} by {book.author} \u2014 {book.available_copies}/{book.total_copies} available")

    print()
    print("Enter ISBN you want to check out:")
    isbn = input()
    catalog.check_out_book(isbn)
    query = input("Search for a book by title: ").strip()
    results = catalog.search_by_title(query)

    def search_by_title(self, title_query):
    normalized = title_query.strip().lower()
    return [
        book for book in self.books
        if normalized in book.title.lower()
    ]

    if not results:
        print("No books found with that title.")
    else:
        print("\nSearch Results:")
        for book in results:
            print(f"{book.title} by {book.author} — {book.available_copies}/{book.total_copies} available")

    checked_out = catalog.find_by_isbn(isbn)
    print(f"'{checked_out.title}' now has {checked_out.available_copies}/{checked_out.total_copies} available.")

    print()
    print(f"Total copies available across catalog: {catalog.total_available_copies()}")


if __name__ == "__main__":
    main()
