from library_app.catalog import Catalog
from library_app.book import Book

def book_checked_out_through_catalog_recorded_due_date():
    # Arrange
    catalog = Catalog()
    book = Book("Clean", "Martin", "111", 3)
    catalog.add_book(book)

    # Act
    catalog.check_out_book("111")
    book.due_date += 14

    # Assert
    assert book.is_overdue == True