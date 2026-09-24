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
        print(f"{book.title} by {book.author} \u2014 ISBN# {book.isbn} {book.available_copies}/{book.total_copies} available")

    print()
    print("Checking out 'Clean Code'...")
    catalog.check_out_book("9780132350884")

    clean_code = catalog.find_by_isbn("9780132350884")
    print(f"'{clean_code.title}' now has {clean_code.available_copies}/{clean_code.total_copies} available.")

    print()
    print(f"Total copies available across catalog: {catalog.total_available_copies()}")


if __name__ == "__main__":
    main()
